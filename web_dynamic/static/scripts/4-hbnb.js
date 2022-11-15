const $ = window.$;
$(document).ready(function () {
  // list all checked amenities
  function getAmenities () {
    const checkedItems = {};
    $('input').click(function () {
      $('input:checkbox:checked').each(function () {
        checkedItems[$(this).attr('data-id')] = $(this).attr('data-name');
      });

      if (!$(this).prop('checked')) {
        delete checkedItems[$(this).attr('data-id')];
      }

      const amenities = Object.values(checkedItems);
      const theRest = `${amenities}`.length > 30 ? '...' : '';
      amenities.length ? $('.amenities h4').text(`${amenities}`.slice(0, 30) + theRest) : $('.amenities h4').html('&nbsp;');
      localStorage.setItem('amenities', JSON.stringify(checkedItems));
    });
  }
  getAmenities();

  // display api status
  $.get('http://0.0.0.0:5001/api/v1/status/', function (data) {
    if (data.status === 'OK') {
      $('#api_status').addClass('available');
      $('.available').removeAttr('id');
    } else {
      $('.available').attr('id', 'api_status');
      $('#api_status').removeClass('available');
    }
  });

  // display places
  function createPlace (data) {
    $.ajax({
      type: 'POST',
      url: 'http://0.0.0.0:5001/api/v1/places_search/',
      data: JSON.stringify(data),
      headers: {
        'Content-Type': 'application/json'
      },
      success: data => {
        for (const place of data) {
          const $article = $('<article />').appendTo('.places');

          // title box
          $article.append(`<div class="title_box"><h2>${place.name}</h2><div class="price_by_night">${place.price_by_night}</div></div>`);

          // information
          const guest = place.max_guest > 1 ? 'Guests' : 'Guest';
          const rooms = place.number_rooms > 1 ? 'Rooms' : 'Room';
          const bathrooms = place.number_bathrooms > 1 ? 'Bathrooms' : 'Bathroom';
          $article.append(`<div class="information">
                <div class="max_guest">${place.max_guest} ${guest}</div>
                <div class="number_rooms">${place.number_rooms} ${rooms}</div>
                <div class="number_bathrooms">${place.number_bathrooms} ${bathrooms}
              </div>`);

          const user = $.ajax({
            url: `http://0.0.0.0:5001/api/v1/users/${place.user_id}`,
            success: user => {
              return user;
            }
          });
          user.done(function (user) {
            // description
            const owner = `<div class="user">${user.first_name} ${user.last_name}</div>`;
            const description = `<div class="description">${place.description}</div>`;
            $article.append(owner + description);
          });
        }
      }
    });
  }
  createPlace({});
  $('button').click(() => {
    $('.places').empty();
    const data = {
      states: [],
      cities: [],
      amenities: Object.keys(JSON.parse(localStorage.getItem('amenities')))
    };
    createPlace(data);
  });
});
