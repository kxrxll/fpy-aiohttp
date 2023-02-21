from db import Ad, Session
from aiohttp import web

routes = web.RouteTableDef()


@routes.view('/ads/{ad_id}')
class Ads_get_delete(web.View):
    async def get(self):
        ad_id = self.request.match_info['ad_id']
        with Session() as session:
            ad = session.query(Ad).get(ad_id)
            session.commit()
            return web.json_response({
                'Heading': ad.heading,
                'Description': ad.description
            })

    async def delete(self):
        ad_id = self.request.match_info['ad_id']
        with Session() as session:
            ad = session.query(Ad).get(ad_id)
            session.delete(ad)
            session.commit()
            return web.json_response({
                'status': 'ok'
            })


@routes.view('/ads/')
class Ads_post(web.View):
    async def post(self):
        json_data = await self.request.json()
        print(json_data)
        with Session() as session:
            new_ad = Ad(**json_data)
            session.add(new_ad)
            session.commit()
            return web.json_response({
                'id': new_ad.id,
                'created at': int(new_ad.date.timestamp())
            })


if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)
