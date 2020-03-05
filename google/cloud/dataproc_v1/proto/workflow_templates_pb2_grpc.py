# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.cloud.dataproc_v1.proto import (
    workflow_templates_pb2 as google_dot_cloud_dot_dataproc__v1_dot_proto_dot_workflow__templates__pb2,
)
from google.longrunning import (
    operations_pb2 as google_dot_longrunning_dot_operations__pb2,
)
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class WorkflowTemplateServiceStub(object):
    """The API interface for managing Workflow Templates in the
  Dataproc API.
  """

    def __init__(self, channel):
        """Constructor.

    Args:
      channel: A grpc.Channel.
    """
        self.CreateWorkflowTemplate = channel.unary_unary(
            "/google.cloud.dataproc.v1.WorkflowTemplateService/CreateWorkflowTemplate",
            request_serializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_workflow__templates__pb2.CreateWorkflowTemplateRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_workflow__templates__pb2.WorkflowTemplate.FromString,
        )
        self.GetWorkflowTemplate = channel.unary_unary(
            "/google.cloud.dataproc.v1.WorkflowTemplateService/GetWorkflowTemplate",
            request_serializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_workflow__templates__pb2.GetWorkflowTemplateRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_workflow__templates__pb2.WorkflowTemplate.FromString,
        )
        self.InstantiateWorkflowTemplate = channel.unary_unary(
            "/google.cloud.dataproc.v1.WorkflowTemplateService/InstantiateWorkflowTemplate",
            request_serializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_workflow__templates__pb2.InstantiateWorkflowTemplateRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
        self.InstantiateInlineWorkflowTemplate = channel.unary_unary(
            "/google.cloud.dataproc.v1.WorkflowTemplateService/InstantiateInlineWorkflowTemplate",
            request_serializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_workflow__templates__pb2.InstantiateInlineWorkflowTemplateRequest.SerializeToString,
            response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
        self.UpdateWorkflowTemplate = channel.unary_unary(
            "/google.cloud.dataproc.v1.WorkflowTemplateService/UpdateWorkflowTemplate",
            request_serializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_workflow__templates__pb2.UpdateWorkflowTemplateRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_workflow__templates__pb2.WorkflowTemplate.FromString,
        )
        self.ListWorkflowTemplates = channel.unary_unary(
            "/google.cloud.dataproc.v1.WorkflowTemplateService/ListWorkflowTemplates",
            request_serializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_workflow__templates__pb2.ListWorkflowTemplatesRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_workflow__templates__pb2.ListWorkflowTemplatesResponse.FromString,
        )
        self.DeleteWorkflowTemplate = channel.unary_unary(
            "/google.cloud.dataproc.v1.WorkflowTemplateService/DeleteWorkflowTemplate",
            request_serializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_workflow__templates__pb2.DeleteWorkflowTemplateRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class WorkflowTemplateServiceServicer(object):
    """The API interface for managing Workflow Templates in the
  Dataproc API.
  """

    def CreateWorkflowTemplate(self, request, context):
        """Creates new workflow template.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetWorkflowTemplate(self, request, context):
        """Retrieves the latest workflow template.

    Can retrieve previously instantiated template by specifying optional
    version parameter.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def InstantiateWorkflowTemplate(self, request, context):
        """Instantiates a template and begins execution.

    The returned Operation can be used to track execution of
    workflow by polling
    [operations.get][google.longrunning.Operations.GetOperation].
    The Operation will complete when entire workflow is finished.

    The running workflow can be aborted via
    [operations.cancel][google.longrunning.Operations.CancelOperation].
    This will cause any inflight jobs to be cancelled and workflow-owned
    clusters to be deleted.

    The [Operation.metadata][google.longrunning.Operation.metadata] will be
    [WorkflowMetadata](https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata).
    Also see [Using
    WorkflowMetadata](https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).

    On successful completion,
    [Operation.response][google.longrunning.Operation.response] will be
    [Empty][google.protobuf.Empty].
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def InstantiateInlineWorkflowTemplate(self, request, context):
        """Instantiates a template and begins execution.

    This method is equivalent to executing the sequence
    [CreateWorkflowTemplate][google.cloud.dataproc.v1.WorkflowTemplateService.CreateWorkflowTemplate], [InstantiateWorkflowTemplate][google.cloud.dataproc.v1.WorkflowTemplateService.InstantiateWorkflowTemplate],
    [DeleteWorkflowTemplate][google.cloud.dataproc.v1.WorkflowTemplateService.DeleteWorkflowTemplate].

    The returned Operation can be used to track execution of
    workflow by polling
    [operations.get][google.longrunning.Operations.GetOperation].
    The Operation will complete when entire workflow is finished.

    The running workflow can be aborted via
    [operations.cancel][google.longrunning.Operations.CancelOperation].
    This will cause any inflight jobs to be cancelled and workflow-owned
    clusters to be deleted.

    The [Operation.metadata][google.longrunning.Operation.metadata] will be
    [WorkflowMetadata](https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata).
    Also see [Using
    WorkflowMetadata](https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).

    On successful completion,
    [Operation.response][google.longrunning.Operation.response] will be
    [Empty][google.protobuf.Empty].
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateWorkflowTemplate(self, request, context):
        """Updates (replaces) workflow template. The updated template
    must contain version that matches the current server version.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListWorkflowTemplates(self, request, context):
        """Lists workflows that match the specified filter in the request.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteWorkflowTemplate(self, request, context):
        """Deletes a workflow template. It does not cancel in-progress workflows.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_WorkflowTemplateServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "CreateWorkflowTemplate": grpc.unary_unary_rpc_method_handler(
            servicer.CreateWorkflowTemplate,
            request_deserializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_workflow__templates__pb2.CreateWorkflowTemplateRequest.FromString,
            response_serializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_workflow__templates__pb2.WorkflowTemplate.SerializeToString,
        ),
        "GetWorkflowTemplate": grpc.unary_unary_rpc_method_handler(
            servicer.GetWorkflowTemplate,
            request_deserializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_workflow__templates__pb2.GetWorkflowTemplateRequest.FromString,
            response_serializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_workflow__templates__pb2.WorkflowTemplate.SerializeToString,
        ),
        "InstantiateWorkflowTemplate": grpc.unary_unary_rpc_method_handler(
            servicer.InstantiateWorkflowTemplate,
            request_deserializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_workflow__templates__pb2.InstantiateWorkflowTemplateRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
        "InstantiateInlineWorkflowTemplate": grpc.unary_unary_rpc_method_handler(
            servicer.InstantiateInlineWorkflowTemplate,
            request_deserializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_workflow__templates__pb2.InstantiateInlineWorkflowTemplateRequest.FromString,
            response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
        ),
        "UpdateWorkflowTemplate": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateWorkflowTemplate,
            request_deserializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_workflow__templates__pb2.UpdateWorkflowTemplateRequest.FromString,
            response_serializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_workflow__templates__pb2.WorkflowTemplate.SerializeToString,
        ),
        "ListWorkflowTemplates": grpc.unary_unary_rpc_method_handler(
            servicer.ListWorkflowTemplates,
            request_deserializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_workflow__templates__pb2.ListWorkflowTemplatesRequest.FromString,
            response_serializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_workflow__templates__pb2.ListWorkflowTemplatesResponse.SerializeToString,
        ),
        "DeleteWorkflowTemplate": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteWorkflowTemplate,
            request_deserializer=google_dot_cloud_dot_dataproc__v1_dot_proto_dot_workflow__templates__pb2.DeleteWorkflowTemplateRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.cloud.dataproc.v1.WorkflowTemplateService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
