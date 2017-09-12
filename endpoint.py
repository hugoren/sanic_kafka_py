from sanic.response import json
from sanic import Blueprint
from utils import auth
from service import zk_node


bp_zk = Blueprint('kafka-center')


@bp_zk.route('/api/v1/kafka/node/', methods=['GET', 'POST'])
@auth('token')
async def node(req):
        data = req.json
        tree_node = data.get('node')
        r = await zk_node(tree_node)
        return json(r)
