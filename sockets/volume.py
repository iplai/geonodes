import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Volume

class Volume(gn.Geometry):
    """ Class Volume
    

    | Inherits from: gn.Geometry 
    Index 
    

    Methods
    =======
    - **to_mesh** : VolumeToMesh mesh (Mesh) 
    """


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def to_mesh(self, voxel_size=None, voxel_amount=None, threshold=None, adaptivity=None, resolution_mode='GRID'):
        """ to_mesh
        

        | Node: VolumeToMesh 
        Top Index 
        

            v = volume.to_mesh(voxel_size, voxel_amount, threshold, adaptivity, resolution_mode) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - volume       : Volume (self) 
            - voxel_size   : Float 
            - voxel_amount : Float 
            - threshold    : Float 
            - adaptivity   : Float 
        

            Parameters arguments
            --------------------
            - resolution_mode : 'GRID' in [GRID, VOXEL_AMOUNT, VOXEL_SIZE] 
        

        Node creation
        =============
        

            node = nodes.VolumeToMesh(volume=self, voxel_size=voxel_size, voxel_amount=voxel_amount, threshold=threshold,
            adaptivity=adaptivity, resolution_mode=resolution_mode) 
        

        Returns
        =======
                Mesh 
        """

        return nodes.VolumeToMesh(volume=self, voxel_size=voxel_size, voxel_amount=voxel_amount, threshold=threshold, adaptivity=adaptivity, resolution_mode=resolution_mode).mesh


