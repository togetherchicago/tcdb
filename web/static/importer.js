$( document ).ready(function() {
    console.log( "ready!" );

    $('.datepicker').datepicker({
        format: 'mm/dd/yyyy',
        autoClose: 'true',
        startDate: '-0d'
    });

    $(function () {
      $('[data-toggle="popover"]').popover()
    });

    $("#dw").click(function(){
        $("#wr").attr("class", "")
        $("#glr").attr("class", "")
        $("#dw").attr("class", "active")
        $("[name=dataset-type]").attr("value", "dw")
    });

    $("#wr").click(function(){
        $("#wr").attr("class", "active")
        $("#glr").attr("class", "")
        $("#dw").attr("class", "")
        $("[name=dataset-type]").attr("value", "wr")
    });

    $("#glr").click(function(){
        $("#wr").attr("class", "")
        $("#glr").attr("class", "active")
        $("#dw").attr("class", "")
        $("[name=dataset-type]").attr("value", "glr")
    });

    $(document).on('change', ':file', function() {
      var input = $(this),
          numFiles = input.get(0).files ? input.get(0).files.length : 1,
          label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
      input.trigger('fileselect', [numFiles, label]);
    });

    $(document).ready( function() {
      $(':file').on('fileselect', function(event, numFiles, label) {
          console.log(numFiles);
          console.log(label);
          $("[name=dataset-file-name]").val(label)
      });
    });

});
