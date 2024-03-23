from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Добро пожаловать на главную страницу!'


@app.route('/news')
@app.route('/news/<string:subpage>')
def news(subpage=None):
    if subpage:
        return f'Здесь вы найдете информацию о разделе "{subpage}" новостей.'
    else:
        return 'Здесь вы найдете последние новости города.'


@app.route('/management')
@app.route('/management/<string:subpage>')
def management(subpage=None):
    if subpage:
        return f'Информация о разделе "{subpage}" руководства города.'
    else:
        return 'Информация о руководстве города.'


@app.route('/facts')
@app.route('/facts/<string:subpage>')
def facts(subpage=None):
    if subpage:
        return f'Интересные факты о разделе "{subpage}" нашего города.'
    else:
        return 'Интересные факты о нашем городе.'


@app.route('/contacts')
@app.route('/contacts/<string:subpage>')
def contacts(subpage=None):
    if subpage:
        return f'Контактные телефоны для раздела "{subpage}" городских служб.'
    else:
        return 'Контактные телефоны городских служб.'


@app.route('/history')
def history():
    return 'Здесь вы найдете общую информацию об истории города.'


@app.route('/history/people')
def history_people():
    return 'Здесь вы найдете информацию об известных жителях города.'


@app.route('/history/photos')
def history_photos():
    return 'Здесь вы найдете исторические фотографии города.'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)

