/**
 * Created by Spencer on 3/7/2015.
 */
$(function(){

    $('#show_login_dialog').on('click', function() {
        $.loadmodal({
            url: '/homepage/index.loginform/',
            title: 'Login'
        });
    });//click

});//ready



$(function(){

    $('#show_logout_dialog').on('click', function() {
        $.loadmodal({
            url: '/homepage/logoutform/',
            title: 'Logout'
        });
    });//click

});//ready


$(function(){

    $('#shoppingcart').on('click', function() {
        $.loadmodal({
            url: '/homepage/shoppingcart.add/',
            title: 'Shopping Cart'
        });
    });//click

});//ready



$(function(){

    $('.add_button').on('click', function(evt) {
        var btn =$(this);
        evt.stopPropagation();

        var pid = $(this).attr('data-pid');
        var id = $(this).id;
        var qty = $("#qty"+pid).val(); //.val

        $.loadmodal({
            url: '/homepage/shoppingcart.add/' + pid + "/" + qty,
            title: 'Shopping Cart'
        });
    });//click

});//ready




$(function(){

    $('#cart').on('click', function() {
        $.loadmodal({
            url: '/homepage/shoppingcart/',
            title: 'Shopping Cart'
        });
    });//click

});//ready