// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();


// isotope js
$(window).on('load', function () {
    $('.filters_menu li').click(function () {
        $('.filters_menu li').removeClass('active');
        $(this).addClass('active');

        var data = $(this).attr('data-filter');
        $grid.isotope({
            filter: data
        })
    });

    var $grid = $(".grid").isotope({
        itemSelector: ".all",
        percentPosition: false,
        masonry: {
            columnWidth: ".all"
        }
    })
});

// nice select
$(document).ready(function() {
    $('select').niceSelect();
  });
//
// /** google_map js **/
// function myMap() {
//     var mapProp = {
//         center: new google.maps.LatLng(40.712775, -74.005973),
//         zoom: 18,
//     };
//     var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
// }

// client section owl carousel
$(".client_owl-carousel").owlCarousel({
    loop: true,
    margin: 0,
    dots: false,
    nav: true,
    navText: [],
    autoplay: true,
    autoplayHoverPause: true,
    navText: [
        '<i class="fa fa-angle-left" aria-hidden="true"></i>',
        '<i class="fa fa-angle-right" aria-hidden="true"></i>'
    ],
    responsive: {
        0: {
            items: 1
        },
        768: {
            items: 2
        },
        1000: {
            items: 2
        }
    }
});

$(document).ready(function() {
    $.ajax({
        url: '/admin/product/get-count-basket-product-types',
        type: "POST",
        contentType: "application/json",
        dataType: 'json',
        accept: '*/*',
        data: JSON.stringify({
                user_id: user_id
            },
            null,
            '\t'
        ),
        success: function(data){
            $('.count_product_types').text(data['count_products'])
        }
    });
  });

$(".add-product-in-basket").click(function (e) {
    e.preventDefault();
    let product_id = $(this).attr('data-product-id')
    $.ajax({
        url: '/admin/product/process-add-from-main',
        type: "POST",
        contentType: "application/json",
        dataType: 'json',
        accept: '*/*',
        data: JSON.stringify({
                product_id: product_id,
                user_id: user_id
            },
            null,
            '\t'
        ),
        success: function(data){
            $('.count_product_types').text(data['count_products'])
        }
    });
})

