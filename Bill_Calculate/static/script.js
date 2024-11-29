$(document).ready(function () {
    // Upload Image
    $('#file-upload').change(function (e) {
        let formData = new FormData();
        formData.append('file', e.target.files[0]);

        $.ajax({
            url: '/upload',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function (data) {
                $('#result').text('Image uploaded successfully. Adjust parameters to proceed.');
                updateProcessedImage(); // Automatically update the image after uploading
            },
            error: function (xhr) {
                alert(xhr.responseText);
            }
        });
    });

    // Function to process image with current slider values
    function updateProcessedImage() {
        let contrast = parseFloat($('#contrast-slider').val());
        let threshold = parseInt($('#threshold-slider').val());
        let resizeFactor = parseFloat($('#resize-slider').val()) / 100;

        $.ajax({
            url: '/process',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ contrast, threshold, resizeFactor }),
            success: function (data) {
                if (data.processed_image_url) {
                    $('#processed-image').attr('src', data.processed_image_url);

                    if (data.items.length > 0) {
                        $('#items-list').html('<h5>Extracted Items</h5>');
                        data.items.forEach((item, index) => {
                            $('#items-list').append(`
                                <div class="mb-3">
                                    <p>${item.item} - $${item.price.toFixed(2)}</p>
                                    <input type="text" class="form-control names-for-item" data-index="${index}" placeholder="Enter names separated by commas">
                                </div>
                            `);
                        });
                    } else {
                        $('#items-list').html('<p>No items found in receipt.</p>');
                    }
                } else {
                    $('#result').text(data.error).addClass('alert-danger');
                }
            },
            error: function (xhr) {
                alert(xhr.responseText);
            }
        });
    }

    // Update image when sliders change
    $('#contrast-slider, #threshold-slider, #resize-slider').on('input', function () {
        updateProcessedImage();
    });

    // Save Parameters
    $('#save-parameters-button').click(function () {
        let parameterName = $('#parameter-name').val().trim();
        if (parameterName === "") {
            alert("Please enter a name for the parameter set.");
            return;
        }

        let contrast = parseFloat($('#contrast-slider').val());
        let threshold = parseInt($('#threshold-slider').val());
        let resizeFactor = parseFloat($('#resize-slider').val()) / 100;

        $.ajax({
            url: '/save_parameters',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ parameter_name: parameterName, contrast, threshold, resizeFactor }),
            success: function (data) {
                alert(data.message);
            },
            error: function (xhr) {
                alert(xhr.responseText);
            }
        });
    });

    // Load Saved Parameters
    $('#load-parameters-button').click(function () {
        $.ajax({
            url: '/load_parameters',
            type: 'GET',
            success: function (data) {
                if (Object.keys(data).length > 0) {
                    let parameterName = prompt("Enter the name of the parameter set to load:\n" + Object.keys(data).join(', '));
                    if (data[parameterName]) {
                        $('#contrast-slider').val(data[parameterName].contrast);
                        $('#threshold-slider').val(data[parameterName].threshold);
                        $('#resize-slider').val(data[parameterName].resize_factor * 100);

                        updateProcessedImage();
                    } else {
                        alert('Parameter set not found.');
                    }
                } else {
                    alert('No saved parameters found.');
                }
            },
            error: function (xhr) {
                alert(xhr.responseText);
            }
        });
    });

    // Add Item Manually
    $('#add-item-button').click(function () {
        let itemName = $('#item-name').val();
        let itemPrice = parseFloat($('#item-price').val());

        if (itemName.trim() === "" || isNaN(itemPrice) || itemPrice <= 0) {
            alert("Please enter a valid item name and price.");
            return;
        }

        $.ajax({
            url: '/add_item',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ item_name: itemName, item_price: itemPrice }),
            success: function (data) {
                if (data.items) {
                    $('#items-list').html('<h5>Extracted Items</h5>');
                    data.items.forEach((item, index) => {
                        $('#items-list').append(`
                            <div class="mb-3">
                                <p>${item.item} - $${item.price.toFixed(2)}</p>
                                <input type="text" class="form-control names-for-item" data-index="${index}" placeholder="Enter names separated by commas">
                            </div>
                        `);
                    });
                } else {
                    $('#result').text(data.error).addClass('alert-danger');
                }
            },
            error: function (xhr) {
                alert(xhr.responseText);
            }
        });
    });

    // Calculate Split
    $('#calculate-split-button').click(function () {
        let discountPercentage = parseFloat($('#discount').val());
        let surchargeAmount = parseFloat($('#surcharge').val());
        let namesForItems = [];

        $('.names-for-item').each(function () {
            namesForItems.push($(this).val());
        });

        if (isNaN(discountPercentage) || isNaN(surchargeAmount)) {
            alert("Please enter valid discount and surcharge values.");
            return;
        }

        $.ajax({
            url: '/calculate_split',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ discount_percentage: discountPercentage, surcharge_amount: surchargeAmount, names_for_items: namesForItems }),
            success: function (data) {
                if (data.total) {
                    let resultHTML = `Subtotal: $${data.subtotal.toFixed(2)}<br>Total After Discount: $${data.total.toFixed(2)}<br><br>Individual Expenses:<br>`;
                    for (const [person, expense] of Object.entries(data.individual_expenses)) {
                        resultHTML += `${person}: $${expense.toFixed(2)}<br>`;
                    }
                    $('#result').html(resultHTML).removeClass('alert-danger').addClass('alert-info');
                } else {
                    $('#result').text(data.error).addClass('alert-danger');
                }
            },
            error: function (xhr) {
                alert(xhr.responseText);
            }
        });
    });
});
