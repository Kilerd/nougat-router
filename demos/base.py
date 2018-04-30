from nougat import Nougat

from nougat_router import Router, Routing, get, param, RestRouting


app = Nougat()

router = Router()


class MainRestRouting(RestRouting):

    @get('/')
    @param('name', str)
    async def static_route(self):
        return 'hello {}'.format(self.params.name)


router.add(MainRestRouting)
app.use(router)

app.run()
