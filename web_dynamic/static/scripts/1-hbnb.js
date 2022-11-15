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
    });

    return checkedItems;
  }
  getAmenities();
});
