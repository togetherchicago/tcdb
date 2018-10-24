$( document ).ready(function() {
    $('.datepicker').datepicker({
        format: 'mm/dd/yyyy',
        autoClose: 'true',
        startDate: '-0d'
    });

    $(function () {
      $('[data-toggle="popover"]').popover()
    });

    var tabs = [
        {id: "cc", desc: "blah"},
        {id: "dw", desc: "Save the \"datawall\" tab (worksheet) in the spreadsheet as a comma-separated values (CSV) file. This data should contain 35 columns, starting with student name and ending with action plan and goal."},
        {id: "wr", descr: "Save the weekly roster tab (the first worksheet) in the spreadsheet as a comma-separated values (CSV) file. This data should contain 10 columns, starting with student id and ending with teacher id."},
        {id: "glr", desc: ""}
    ];

    tabs.forEach(function(tab) {
      $("#" + tab.id).click(function(){

          // Deselect all tabs
          tabs.forEach(function(e) {
            $("#" + tab.id).attr("class", "")
          })

          // Select this tab
          $("#" + tab.id).attr("class", "active")
          $("[name=dataset-type]").attr("value", tab.id)
          $("#dataset-descriptor").text(tab.desc)
      });
    });

    $(document).on('change', ':file', function() {
      var input = $(this),
          numFiles = input.get(0).files ? input.get(0).files.length : 1,
          label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
      input.trigger('fileselect', [numFiles, label]);
    });

    $(document).ready( function() {
      $(':file').on('fileselect', function(event, numFiles, label) {
          $("[name=dataset-file-name]").val(label)
      });
    });

    $("#dataset-descriptor").text("Save the weekly roster tab (the first worksheet) in the spreadsheet as a comma-separated values (CSV) file. This data should contain 10 columns, starting with student id and ending with teacher id.")

});
