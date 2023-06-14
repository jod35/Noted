from fastapi import APIRouter

noteb_router = APIRouter(
    tags=["notebooks"]
)


@noteb_router.get('/')
async def get_all_notebooks():
    pass

@noteb_router.get('/{notebook_id}')
async def get_all_notebooks(notebook_id:int):
    """retrieve a notebook by ID

    Args:
        notebook_id (int): ID of notebook to be retrieved
    """
    pass

@noteb_router.put('/{notebook_id}')
async def update_notebook(notebook_id:int):
    """Update notebook

        ### Parameters
        notebook_id (int): an ID for the notebook to update
    """
    pass

@noteb_router.patch('/{notebook_id}')
async def partially_update_notebook(notebook_id:int):
    """partially Update notebook

        ### Parameters
        notebook_id (int): an ID for the notebook to partially update
    """
    pass

@noteb_router.delete('/{notebook_id}')
async def delete_notebook(notebook_id:int):
    """delete notebook

        ### Parameters
        notebook_id (int): an ID for the notebook to delete
    """
    pass