$(document).ready(function() {
    $('#imageInput').change(function() {
        var reader = new FileReader();
        reader.onload = function(e) {
            $('#imagePreview').attr('src', e.target.result).show();
            $('#scanLine').show();
        };
        reader.readAsDataURL(this.files[0]);
    });

    $('#uploadForm').submit(function(event) {
        event.preventDefault();
        $('#scanLine').css('display', 'none');
        var formData = new FormData(this);
        $.ajax({
            type: 'POST',
            url: '/predict',
            data: formData,
            contentType: false,
            processData: false,
            success: function(response) {
                $('#result').html(`<p class="alert alert-info">${response.result}</p>`);
            }
        });
    });
});
