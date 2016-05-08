var $ = require('jquery');
export default function navbar() {
  var $navbar = $("#navbar"),
        y_pos = $navbar.offset().top,
        height = $navbar.height();

        $(document).scroll(function() {
        var scrollTop = $(this).scrollTop();

        if (scrollTop > y_pos + height) {
            $navbar.addClass("menu-fixed").animate({
                top: 0
            });
        } else if (scrollTop <= y_pos) {
            $navbar.removeClass("menu-fixed").clearQueue().animate({
                top: "-30px"
            }, 0);
        }
    });
};
