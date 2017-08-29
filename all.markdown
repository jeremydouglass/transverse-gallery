---
layout: default
title:  "All"
date:   2017-08-28
categories: galley
---

# All Works

This gallery presents the complete collection of works mapped to-date in collection-order.


## Gallery

<ul class="photo-gallery">
{% for image in site.static_files %}
  {% if image.path contains 'assets/images' %}
  <a href="{{ site.baseurl }}{{ image.path }}"><img src="{{ site.baseurl }}/assets/thumbs/{{ image.name }}" alt="image" onload="this.width/=4;this.onload=null;"/></a>
  {% endif %}
{% endfor %}
</ul>

