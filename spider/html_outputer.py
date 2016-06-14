# encoding: utf-8

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w')
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')

        for data in self.datas:
            title = data['title'].encode('utf-8')
            summary = data['summary'].encode('utf-8')
            fout.write('<tr>')
            fout.write('<td>%s</td>'% data['url'])
            fout.write('<td>%s</td>'% title)
            fout.write('<td>%s</td>'% summary)
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')

        fout.close()