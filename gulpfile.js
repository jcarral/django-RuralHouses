var gulp = require('gulp');
var sass = require('gulp-sass');
var sourcemaps = require('gulp-sourcemaps');
var autoprefixer = require('gulp-autoprefixer');
var watch = require('gulp-watch');
var minifycss = require('gulp-minify-css');
var rename = require('gulp-rename');
var gzip = require('gulp-gzip');
var livereload = require('gulp-livereload');
var watchify = require('watchify');
var browserify = require('browserify');
var babelify = require('babelify');
var source = require('vinyl-source-stream');
var gutil = require('gulp-util');
var buffer = require('vinyl-buffer');


var gzip_options = {
    threshold: '1kb',
    gzipOptions: {
        level: 9
    }
};
/* Compile Our Sass */
gulp.task('sass', function() {
    return gulp.src('src/css/*.scss')
        .pipe(sass())
        .pipe(autoprefixer())
        .pipe(gulp.dest('static/css'))
        .pipe(rename({suffix: '.min'}))
        .pipe(minifycss())
        .pipe(autoprefixer())
        .pipe(gulp.dest('static/css'))
        .pipe(gzip(gzip_options))
        .pipe(gulp.dest('static/css'))
        .pipe(livereload());
});

gulp.task('build:js', function() {
 var bundler = watchify(browserify({ entries: 'src/scripts/main.js', debug: true }, watchify.args));

 bundler.transform(babelify, { presets: ['es2015'] });
 bundler.on('update', rebundle);
 return rebundle();

 function rebundle() {
   var start = Date.now();
   return bundler.bundle()
     .on('error', function(err) {
       gutil.log(gutil.colors.red(err.toString()));
     })
     .on('end', function() {
       gutil.log(gutil.colors.green('Finished rebundling in', (Date.now() - start) + 'ms.'));
     })
     .pipe(source('bundle.js'))
     .pipe(buffer())
     .pipe(sourcemaps.init({ loadMaps: true }))
     .pipe(sourcemaps.write('.'))
     .pipe(gulp.dest('static/js/'));
 }
});


/* Watch Files For Changes */
gulp.task('watch', ['build:js'], function() {
    livereload.listen();
    gulp.watch('src/css/*.scss', ['sass']);
});

gulp.task('default', ['sass', 'watch']);
