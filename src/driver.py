from cloudshell.shell.core.resource_driver_interface import ResourceDriverInterface
from ixia_handler import IxiaHandler
from cloudshell.shell.core.context_utils import get_resource_name

class IxLoadControllerDriver(ResourceDriverInterface):

    def __init__(self):
        self.handler = IxiaHandler()

    def initialize(self, context):
        """
        :param context: ResourceCommandContext,ReservationContextDetailsobject with all Resource Attributes inside
        :type context:  context: cloudshell.shell.core.driver_context.ResourceRemoteCommandContext
        """

        self.handler.initialize(context)
        return ""

    def get_inventory(self, context):
        """ Return device structure with all standard attributes

        :type context: cloudshell.shell.core.driver_context.AutoLoadCommandContext
        :rtype: cloudshell.shell.core.driver_context.AutoLoadDetails
        """

        return self.handler.get_inventory(context)


    def load_config(self, context, ixia_config_file_name):
        """ Load STC configuration file and reserve ports.
        :param context: the context the command runs on
        :type context: cloudshell.shell.core.driver_context.ResourceRemoteCommandContext
        :param get_data_from_config: True - reserve physical ports saved in the configuration file
                                     False - reserve physical ports from sandbox.
        """

        my_api = self.handler.get_api(context)
        reservation_id = context.reservation.reservation_id
        resource_name = get_resource_name(context=context)
        #my_api.EnqueueCommand(reservationId=reservation_id,targetName=resource_name,commandName="keep_alive", targetType="Resource")

        self.handler.load_config(context, ixia_config_file_name)
        return ""


    def start_test(self, context,blocking):
        """
        :param context: the context the command runs on
        :type context: cloudshell.shell.core.driver_context.ResourceRemoteCommandContext
        """

        self.handler.start_test(context,blocking)
        return ""

    def stop_test(self, context):
        """
        :param context: the context the command runs on
        :type context: cloudshell.shell.core.driver_context.ResourceRemoteCommandContext
        """

        self.handler.stop_test(context)
        return ""

    def get_statistics(self, context, view_name,output_type):
        self.handler.get_statistics(context, view_name, output_type)
        return ""

    def cleanup(self):
        self.handler.tearDown()
        pass


    def keep_alive(self, context, cancellation_context):

        while not cancellation_context.is_cancelled:
            pass
        if cancellation_context.is_cancelled:
            self.handler.tearDown()




