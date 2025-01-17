/*! Set focus on "id_name" element on document load and cursor to end of text
 * Provides for easier editing
 */
window.onload = function() {
  const textBoxName = document.getElementById("id_name");
  textBoxName.focus();
  textBoxName.setSelectionRange(textBoxName.value.length, textBoxName.value.length);
}
