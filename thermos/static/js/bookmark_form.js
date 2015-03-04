$(document).ready(function() {
  var _tags = {{ all_tags()|map(attribute='name'|list|tojson|safe) }};

  $('#tags').select2({ tags: _tags, tokenSeparators: [",", " "]});
});

