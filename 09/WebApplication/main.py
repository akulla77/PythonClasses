import uuid

from pathlib import Path
from typing import Any, AsyncIterable, Dict, Iterable

from aiohttp import web
from aiohttp_swagger import *

import aiohttp_jinja2
import jinja2

from notes.Note import Note
from notes.Storage import AbstractStorage, StorageFactory


routes = web.RouteTableDef()


async def __to_list(iterable: AsyncIterable[Any]) -> Iterable[Any]:
    return [item async for item in iterable]


@routes.get('/')
async def root(_) -> web.Response:
    raise web.HTTPFound(location='/notes')


@routes.get('/notes')
@aiohttp_jinja2.template('notes.jinja2')
async def get_notes(request: web.Request) -> Dict[str, Any]:
    storage: AbstractStorage = request.app['storage']
    return {'notes': await __to_list(storage.get_all())}


@routes.post('/notes')
async def add_object(request: web.Request) -> web.Response:
    storage: AbstractStorage = request.app['storage']

    data = dict(await request.post())
    note = Note(**data | {'id': uuid.uuid4()})
    await storage.put_one(note)

    return web.HTTPFound(location=f'/notes')


@routes.get('/api/notes')
async def get_notes(request: web.Request) -> web.Response:
    """
    description: Получить список заметок.
    tags:
    - notes
    produces:
    - application/json
    responses:
        "200":
            description: возвращает список заметок
    """

    storage: AbstractStorage = request.app['storage']
    notes = [note.to_json() async for note in storage.get_all()]

    return web.json_response(notes)


@swagger_path('docs/get_note.yml')
@routes.get('/api/notes/{note_id}')
async def get_note(request: web.Request) -> web.Response:
    storage: AbstractStorage = request.app['storage']
    key = request.match_info['note_id']
    note = await storage.get_one(key)

    return web.json_response(note.to_json()) if note else web.HTTPNotFound()


@swagger_path('docs/add_note.yml')
@routes.post('/api/notes')
async def add_note(request: web.Request) -> web.Response:
    storage: AbstractStorage = request.app['storage']

    try:
        data = dict(await request.json())
        note = Note(**data | {'id': uuid.uuid4()})
    except Exception as error:
        return web.HTTPBadRequest(reason=str(error))

    await storage.put_one(note)

    return web.HTTPCreated(headers={'Location': f'/api/notes/{note.id}'})


@swagger_path('docs/update_note.yml')
@routes.put('/api/notes/{note_id}')
async def update_note(request: web.Request) -> web.Response:
    storage: AbstractStorage = request.app['storage']
    key: uuid = request.match_info['note_id']

    if note := await storage.get_one(key):
        try:
            data = dict(await request.json())
            note = Note(**note.to_json() | data)
        except Exception as error:
            return web.HTTPBadRequest(reason=str(error))

        await storage.put_one(note)
        return web.HTTPNoContent()

    return web.HTTPNotFound()


@swagger_path('docs/delete_note.yml')
@routes.delete('/api/notes/{note_id}')
async def delete_note(request: web.Request) -> web.Response:
    storage: AbstractStorage = request.app['storage']
    key: uuid = request.match_info['note_id']

    if await storage.contains(key):
        await storage.delete_one(key)
        return web.HTTPNoContent()
    else:
        return web.HTTPNotFound()


if __name__ == '__main__':
    settings = {
        'port': 8080,
        'data_storage': {
            'storage': 'memory',
        }
    }

    templates_directory = Path(__file__).parent.joinpath('templates')

    app = web.Application()
    app['storage'] = StorageFactory.create_storage(settings['data_storage'])

    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(templates_directory)))
    app.add_routes(routes)

    setup_swagger(app, title='Notes API')

    web.run_app(app, host='localhost', port=settings['port'])
