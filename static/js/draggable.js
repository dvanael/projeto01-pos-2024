$(function() {
    const $draggable = $("#draggable");
    const originalPosition = $draggable.position();

    $("#draggable").draggable({
        stop: function() {
            setTimeout(function() {
                $("#draggable").animate({
                    top: originalPosition.top,
                    left: 0,
                }, 500);
            }, 1500);
        }
    });
});
