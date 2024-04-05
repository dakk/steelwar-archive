import venom

class RotationAnimator:
	def __init__( self, rot ):
		self.animator = venom.CreateRotationAnimator( rot )
		
	def SetRotation( self, rot ):
		venom.SetRotationAnimatorRotation( self.animator, rot )
	
	def GetRotation( self ):
		return venom.GetRotationAnimatorRotation( self.animator )
		
class CollisionAnimator:
	def __init__( self, selector ):
		self.animator = venom.CreateCollAnimator( selector, self.node )
		self.SetRadius( ( 10.0, 25.0, 10.0 ) )
		self.SetGravity( ( 0.0, -170.0, 0.0 ) )
		self.SetPosition( ( 0.0, 0.0, 0.0 ) )
		
	def SetRadius( self, radius ):
		venom.SetCollAnimtorRadius( self.animator, radius )
		
	def SetGravity( self, gravity ):
		venom.SetCollAnimatorGravity( self.animator, gravity )

	def SetPosition( self, position ):
		venom.SetCollAnimatorPosition( self.animator, position )
	
	def SetVelocity( self, velocity ):
		venom.SetCollAnimatorVelocity( self.animator, velocity )	
	