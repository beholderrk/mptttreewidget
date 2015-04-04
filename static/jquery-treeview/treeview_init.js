(function($){
    $(function(){
        $("ul.manage-treeview").treeview({
            collapsed: true,
            persist: "cookie",
            cookieId: "treeview-control",
            control: ".treeview-control"
        });
    });
})(django.jQuery);