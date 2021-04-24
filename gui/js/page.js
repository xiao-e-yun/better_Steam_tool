"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const $ = require("jquery");
window.onresize = function () {
    window.resizeTo(300, 600);
};
footer = $('footer');
main = $('main#main_contant');
page = {};
$('#menu_toggle').on('mousedown', function () {
    footer.slideToggle();
});
footer.on('click', 'button', function () {
    footer.slideUp();
    load_page(this.id);
});
function load_page(id, href = false) {
    console.log("open \"" + id + "\" page");
    page[id] = {};
    $page = page[id];
    $.get("/page/" + id + ".html", function (data) {
        main.off(); //刪除監聽
        main.html(data);
        $.getScript("/js/" + id + ".js");
    });
}
//# sourceMappingURL=page.js.map