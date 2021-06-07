// on select hit django view  

$.ajaxSetup({
  data: {csrfmiddlewaretoken: '{{ csrf_token }}' },
});

$('select').on('change', function() {
	SearchUrl = "/weather_app/get_weather_info/"
	city = this.value;
	get_api_data(SearchUrl,city)
	$("#forcast_table tbody").remove()

});

function get_forcast(){
	var select_id = document.getElementById("select_id");
	var city =select_id.options[select_id.selectedIndex].value;
	SearchUrl = "/weather_app/get_weather_forcast/"
	get_api_data(SearchUrl,city)
}


function get_api_data(SearchUrl,city){
	$.ajax({

        url: SearchUrl,
        type:'POST', 
        data: {
        	csrfmiddlewaretoken: window.CSRF_TOKEN,
        	city: city
        },
        success: function(data){
        	if (data['forcast']== true)
        	{
        		generate_forcast_table(data);
        	}
        	else
        	{
        		    insert_data_into_card(data);
        	}
      }
    });
}

function generate_forcast_table(data){

	 	// var forcast_data = $.parseJSON(data["Bills"]);

   //      forcast_data=$.parseJSON(Bills)
   		console.log(data);
        var items = [];
        $.each(data['list'],function( key, val ) {
        items.push("<tr>");
        items.push("<td>"+data['list'][key].dt_txt+"</td>");
        items.push("<td>"+data['list'][key]['main'].humidity+"</td>");
        items.push("<td>"+data['list'][key]['main'].pressure+"</td>");
        items.push("<td>"+data['list'][key]['main'].temp+"</td>");
        items.push("<td>"+data['list'][key]['weather']['0'].description+"</td>");

        items.push("</tr>");

        });
        $("#forcast_table tbody").remove()
        $( "<tbody/>", {
        html: items.join("")
        }).appendTo("#forcast_table");
}

function insert_data_into_card(data)
{
		$('#country_code').text(data.country_code);
        $('#coordinate').text(data.coordinate);
        $('#temp').text(data.temp);
        $('#pressure').text(data.pressure);
        $('#humidity').text(data.humidity);
        $('#main').text(data.main);
        $('#description').text(data.description);
}

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else { 
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {
	
    SearchUrl = "/weather_app/get_weather_info_coordinate/"
	$.ajax({

        url: SearchUrl,
        type:'POST', 
        data: {
        	csrfmiddlewaretoken: window.CSRF_TOKEN,
        	latitude: position.coords.latitude,
        	longitude: position.coords.longitude
        },
        success: function(data){
        console.log(data.coordinate)
        insert_data_into_card(data);

      }
    });

}
