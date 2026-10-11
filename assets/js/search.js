(function () {
  var params = new URLSearchParams(window.location.search);
  var q = (params.get("q") || "").trim();
  var input = document.getElementById("search-page-input");
  var status = document.getElementById("search-status");
  var list = document.getElementById("search-results");
  if (input) input.value = q;
  if (!q) { status.textContent = "Type a word to search every edition."; return; }

  status.textContent = "Searching…";
  fetch(window.ESSCHER_INDEX)
    .then(function (r) { return r.json(); })
    .then(function (items) {
      var terms = q.toLowerCase().split(/\s+/).filter(Boolean);
      var hits = items.filter(function (it) {
        var hay = (it.title + " " + it.text).toLowerCase();
        return terms.every(function (t) { return hay.indexOf(t) !== -1; });
      });
      status.textContent = hits.length === 1 ? "1 result." : hits.length + " results.";
      hits.forEach(function (it) {
        var li = document.createElement("li");
        var date = document.createElement("span");
        date.className = "mono small muted";
        date.textContent = it.date;
        var tag = document.createElement("span");
        tag.className = "tag";
        tag.textContent = it.edition === "weekly" ? "Weekly" : (it.edition === "story" ? "Story" : "Daily");
        var a = document.createElement("a");
        a.href = it.url;
        a.textContent = it.title;
        li.appendChild(date); li.appendChild(tag); li.appendChild(a);
        list.appendChild(li);
      });
    })
    .catch(function () { status.textContent = "Search is unavailable right now."; });
})();
