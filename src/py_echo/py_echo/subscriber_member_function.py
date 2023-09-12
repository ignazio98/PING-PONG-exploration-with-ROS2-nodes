import rclpy
from rclpy.executors import SingleThreadedExecutor
from class_object.server import Server as s

def main(args=None):
    rclpy.init(args=args)

    subscriber = s.Server()
    executor = SingleThreadedExecutor()
    executor.add_node(subscriber)

    try:
        executor.spin()
    except KeyboardInterrupt:
        subscriber.get_logger().info('Keyboard interrupt, shutting down.\n')
    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
