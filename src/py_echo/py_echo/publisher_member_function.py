import rclpy
from .class_object.Publisher import Client

def main(args=None):
	rclpy.init(args=args)
	
	publisher = Client()
	
	rclpy.spin(publisher)
	rclpy.shutdown()
	return 

if __name__ == '__main__':
    main()
