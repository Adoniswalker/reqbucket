/**
 * Created by adonis on 11/25/17.
 */
$("#my_copy").click(function () {
    $("#my_json").select();
    document.execCommand('copy');
});
function copy_to_clipboard(text_box_id) {
    $(text_box_id).select();
    document.execCommand('copy');
}
// var xhttp;
// if (window.XMLHttpRequest){
//     xhttp = new XMLHttpRequest();
// }else {
//     // code for IE6, IE5
//     xhttp = new ActiveXObject("Microsoft.XMLHTTP");
// }
// xhttp.open("GET", "ajax_info.txt", true);
// xhttp.send();
// $(document).ready(function(){
//   $("#demo").on("hide.bs.collapse", function(){
//     $(".btn").html('<span class="glyphicon glyphicon-collapse-down"></span> Open');
//   });
//   $("#demo").on("show.bs.collapse", function(){
//     $(".btn").html('<span class="glyphicon glyphicon-collapse-up"></span> Close');
//   });
// });
  window.fbAsyncInit = function() {
    FB.init({
      appId      : '{your-app-id}',
      cookie     : true,
      xfbml      : true,
      version    : '{latest-api-version}'
    });

    FB.AppEvents.logPageView();

  };

  (function(d, s, id){
     var js, fjs = d.getElementsByTagName(s)[0];
     if (d.getElementById(id)) {return;}
     js = d.createElement(s); js.id = id;
     js.src = "https://connect.facebook.net/en_US/sdk.js";
     fjs.parentNode.insertBefore(js, fjs);
   }(document, 'script', 'facebook-jssdk'));
