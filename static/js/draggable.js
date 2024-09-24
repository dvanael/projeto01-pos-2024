$(function() {
    const $draggable = $("#draggable");
    const originalPosition = $draggable.position();

    $draggable.draggable({
        start: function() {
            $("body").addClass("move");
            $draggable.addClass("box-shadow")
        },

        stop: function() {
            $("body").removeClass("move");
            $draggable.removeClass("box-shadow")
            setTimeout(function() {
                $("#draggable").animate({
                    top: originalPosition.top,
                    left: 0,
                }, 500);
            }, 1500);
        }
    });
});
