/*! DataTables Custom Display Length Function
 * Set the available display lengths on document load
 */
$(document).ready(function() {
    $('#bootstrapdatatable').DataTable({
      "aLengthMenu": [[10, 25, 50, 100, -1], [10, 25, 50, 100, "All"]],
        "iDisplayLength": 10
       }
    );
} );
