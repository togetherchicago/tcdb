$( document ).ready(function() {
    console.log( "ready!" );

    $('.datepicker').datepicker();
    $('.datepicker').datepicker({
        format: 'mm/dd/yyyy',
        startDate: '-3d'
    });

});
