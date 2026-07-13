// Enable right-to-left layout on Hebrew (and other RTL) pages.
// Material for MkDocs flips its layout when the <html> element has dir="rtl".
// The i18n plugin sets lang="he" but not the dir attribute, so we set it here.
(function () {
  var rtlLangs = ["he", "ar", "fa", "ur"];
  var lang = (document.documentElement.getAttribute("lang") || "").slice(0, 2);
  if (rtlLangs.indexOf(lang) !== -1) {
    document.documentElement.setAttribute("dir", "rtl");
  }
})();
