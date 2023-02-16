from flask import Flask, jsonify, request
from flask.views import MethodView
from db import Ad, Session

app = Flask('app')


class Ads(MethodView):
    def get(self, ad_id: int):
        with Session() as session:
            ad = session.query(Ad).get(ad_id)
            session.commit()
            return jsonify({
                'Heading': ad.heading,
                'Description': ad.description
            })

    def post(self):
        json_data = request.json
        with Session() as session:
            new_ad = Ad(**json_data)
            session.add(new_ad)
            session.commit()
            return jsonify({
                'id': new_ad.id,
                'created at': int(new_ad.date.timestamp())
            })

    def delete(self, ad_id: int):
        with Session() as session:
            ad = session.query(Ad).get(ad_id)
            session.delete(ad)
            session.commit()
            return jsonify({
                'status': 'ok'
            })


app.add_url_rule('/ads/<int:ad_id>',
                 view_func=Ads.as_view('ads'),
                 methods=['GET', 'DELETE']
                 )
app.add_url_rule('/ads/',
                 view_func=Ads.as_view('ads_add'),
                 methods=['POST']
                 )

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
