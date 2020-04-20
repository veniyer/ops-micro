import io
import json
import logging

import importlib.util

import {{ module }}

from fdk import response


def handler(ctx, data: io.BytesIO=None):
    called_fn_response = ""
    try:
        body = json.loads(data.getvalue())
        name = body.get("{{parameters}}")

        called_fn_response = {{ module }}.{{function}}({{parameters}})

    except (Exception, ValueError) as ex:
        logging.getLogger().info('error parsing json payload: ' + str(ex))

    logging.getLogger().info("Inside Python Hello World function")
    return response.Response(
        ctx, response_data=json.dumps(
            {"message": "{0}".format(called_fn_response)}),
        headers={"Content-Type": "application/json"}
    )
