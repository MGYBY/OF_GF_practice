# The 2D simulation with cyclic end BC.

Reason for using cyclic BC: 
1. the `zeroGradient` BC does not work well for 3D cases. 
2. and the domain could be extended using coarse mesh in the lee-side of the cylinder for long-time simulation.
