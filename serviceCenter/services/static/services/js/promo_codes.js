$(".active-discount").each(function () {
    var discountSpan = $(this).find(".discount");
    var discountValue = parseInt(discountSpan.text());
    $({ value: 0 }).animate(
        { value: discountValue },
        {
            duration: 2000,
            step: function () {
                discountSpan.text(Math.floor(this.value) + 1 + "%");
            },
            complete: function () {
                discountSpan
                    .animate({ fontSize: "2em" }, 500)
                    .animate({ color: "red" }, 500)
                    .delay(250)
                    .animate({ fontSize: "1em", color: "black" }, 500);
            }
        }
    );
});
