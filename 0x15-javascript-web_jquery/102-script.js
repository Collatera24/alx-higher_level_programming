// fetches and prints how to say “Hello” depending on the language

$(document).ready(function() {
	$('#btn_translate').click(function() {
		var languageCode = $('#language_code').val();
		var apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + languageCode;

		$.get(apiUrl, function(data) {
			$('#hello').text(data.hello);
		}).fail(function() {
			$('#hello').text('Error fetching translation');
		});
	});
});
