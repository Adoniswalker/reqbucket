$(function () {
    var $endpoints = $('#endpoints');
    var endpointTemplate = $('#endpoints-template').html();
    var $url_name = $('#id_url_name');
    var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    // console.log($crf_token);
    var $json_response = $('#id_json_response');


    function add_end(endpoint) {
        endpoint.end_count = endpoint.requests.length;
        $endpoints.append(Mustache.render(endpointTemplate, endpoint));
    }

    $.ajax({
        type: "GET",
        url: "/api/endpoint/",
        success: function (endpoints) {
            if (endpoints.next) {
                // sets the next icon if there are more endpoints not loaded
                $("#right_endpoint").attr("href", endpoints.next);
            }
            if (endpoints.previous) {
                // sets the back url if person has moved backward
                $('#left_endpoint').attr("href", endpoints.previous);
            }

            $.each(endpoints.results, function (i, result) {
                // console.log("How many");
                add_end(result);
            });
        },
        error: function () {
            alert("Not able to get end points");
        }
    });
    $('#id_new_endpoint').on('click',function () {
        var newEndpoint = {
            url_name: $url_name.val(),
            json_response: $json_response.val()
        };
        $.ajax({
            type: "POST",
            url: "/api/endpoint/",
            data: newEndpoint,
            headers:{"X-CSRFToken": $crf_token},
            success: function (newEnd) {
                add_end(newEnd);
            },
            error: function () {
                alert("There was an error")
            }
        });
    });
    $('.delete').on('click', 'span',function () {
        alert("Delete clicked");
    });

});
