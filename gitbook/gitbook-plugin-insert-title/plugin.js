require(['gitbook', 'jQuery'], function (gitbook, $) {
  var url = ''
  var title = ''
  var style = ''
  var insertLogo = function (url, title, style) {
    var logo = url ? '<img src="' + url + '" style="' + style + '"></img>' : ''
    var ttl = title ? '<p class="title-label">' + title + '</p>' : ''
    $('.book-summary').children().eq(0).before('<div class="book-logo">' + logo + ttl + '</div>')
  }
  gitbook.events.bind('start', function (e, config) {
    url = config['insert-title']['url']
    title = config['insert-title']['title']
    style = config['insert-title']['style']
  })

  gitbook.events.bind("page.change", function() {
    insertLogo(url, title, style)
  })
})
