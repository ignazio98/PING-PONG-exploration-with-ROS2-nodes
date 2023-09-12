import rclpy
from class_object.client import Client as c

def main(args=None):
	rclpy.init(args=args)
	
	publisher = c.Client()
	
	rclpy.spin(publisher)
	rclpy.shutdown()
	return 

if __name__ == '__main__':
    main()
