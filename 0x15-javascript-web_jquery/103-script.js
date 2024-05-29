//fetches and prints how to say “Hello” depending on the language
// And press ENTER

$(document).ready(function() {
	function fetchHello() {
		var languageCode = $('#language_code').val();
		var apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + languageCode;

		$.get(apiUrl, function(data) {
			$('#hello').text(data.hello);
		}).fail(function() {
			$('#hello').text('Error fetching translation');
		});
	}

	$('#btn_translate').click(function() {
		fetchHello();
	});

	$('#language_code').keypress(function(event) {
		if (event.which === 13) { // 13 is the Enter key
			fetchHello();
		}
	});
});
