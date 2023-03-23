"""H1st IoT Data Management: API views."""


from rest_framework.authentication import (BasicAuthentication,
                                           RemoteUserAuthentication,
                                           SessionAuthentication,
                                           TokenAuthentication)
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.renderers import CoreJSONRenderer, JSONRenderer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from silk.profiling.profiler import silk_profile

from k1st_contrib.iot_mgmt.data.filters import (
    DataTypeFilter,
    NumericMeasurementUnitFilter,
    EquipmentDataFieldTypeFilter,
    EquipmentGeneralTypeFilter,
    EquipmentDataFieldFilter,
    EquipmentUniqueTypeGroupFilter,
    EquipmentUniqueTypeFilter,
    EquipmentFacilityFilter,
    EquipmentInstanceFilter,
    EquipmentSystemFilter,
)
from k1st_contrib.iot_mgmt.data.querysets import (
    DATA_TYPE_QUERYSET,
    NUMERIC_MEASUREMENT_UNIT_QUERYSET,
    EQUIPMENT_DATA_FIELD_TYPE_QUERYSET,
    EQUIPMENT_GENERAL_TYPE_QUERYSET,
    EQUIPMENT_DATA_FIELD_REST_API_QUERYSET,
    EQUIPMENT_UNIQUE_TYPE_GROUP_REST_API_QUERYSET,
    EQUIPMENT_UNIQUE_TYPE_REST_API_QUERYSET,
    EQUIPMENT_FACILITY_REST_API_QUERYSET,
    EQUIPMENT_INSTANCE_REST_API_QUERYSET,
    EQUIPMENT_SYSTEM_REST_API_QUERYSET,
)
from k1st_contrib.iot_mgmt.data.serializers import (
    DataTypeSerializer,
    NumericMeasurementUnitSerializer,
    EquipmentDataFieldTypeSerializer,
    EquipmentGeneralTypeSerializer,
    EquipmentDataFieldSerializer,
    EquipmentUniqueTypeGroupSerializer,
    EquipmentUniqueTypeSerializer,
    EquipmentFacilitySerializer,
    EquipmentInstanceSerializer,
    EquipmentSystemSerializer,
)


class DataTypeViewSet(ReadOnlyModelViewSet):
    """DataTypeViewSet.

    list:
    `GET` an filterable, unpaginated list of 2 Data Types named "cat" and "num"

    retrieve:
    `GET` the Data Type specified by `name` "cat" or "num"
    """

    queryset = DATA_TYPE_QUERYSET

    serializer_class = DataTypeSerializer

    authentication_classes = (
        BasicAuthentication,
        RemoteUserAuthentication,
        SessionAuthentication,
        TokenAuthentication,
    )

    permission_classes = (IsAuthenticatedOrReadOnly,)

    filter_class = DataTypeFilter

    ordering_fields = ('name',)

    ordering = ('name',)

    pagination_class = None

    lookup_field = 'name'

    lookup_url_kwarg = 'data_type_name___cat_or_num'

    renderer_classes = CoreJSONRenderer, JSONRenderer

    @silk_profile(name='API: Data Types')
    def list(self, request, *args, **kwargs):
        """List items."""
        return super().list(request, *args, **kwargs)

    @silk_profile(name='API: Data Type')
    def retrieve(self, request, *args, **kwargs):
        """Retrieve 1 item."""
        return super().retrieve(request, *args, **kwargs)


class NumericMeasurementUnitViewSet(ModelViewSet):
    """NumericMeasurementUnitViewSet.

    list:
    `GET` a filterable, unpaginated list of Numeric Measurement Units

    retrieve:
    `GET` the Numeric Measurement Unit specified by `name`

    create:
    `POST` a new Numeric Measurement Unit by `name`

    update:
    `PUT` updated data for the Numeric Measurement Unit specified by `name`

    partial_update:
    `PATCH` the Numeric Measurement Unit specified by `name`

    destroy:
    `DELETE` the Numeric Measurement Unit specified by `name`
    """

    queryset = NUMERIC_MEASUREMENT_UNIT_QUERYSET

    serializer_class = NumericMeasurementUnitSerializer

    authentication_classes = (
        BasicAuthentication,
        RemoteUserAuthentication,
        SessionAuthentication,
        TokenAuthentication,
    )

    permission_classes = (IsAuthenticatedOrReadOnly,)

    filter_class = NumericMeasurementUnitFilter

    ordering_fields = ('name',)

    ordering = ('name',)

    pagination_class = None

    lookup_field = 'name'

    lookup_url_kwarg = 'numeric_measurement_unit_name'

    renderer_classes = CoreJSONRenderer, JSONRenderer

    @silk_profile(name='API: Numeric Measurement Units')
    def list(self, request, *args, **kwargs):
        """List items."""
        return super().list(request, *args, **kwargs)

    @silk_profile(name='API: Numeric Measurement Unit')
    def retrieve(self, request, *args, **kwargs):
        """Retrieve 1 item."""
        return super().retrieve(request, *args, **kwargs)


class EquipmentDataFieldTypeViewSet(ReadOnlyModelViewSet):
    """EquipmentDataFieldTypeViewSet.

    list:
    `GET` an unfiltered, unpaginated list of Equipment Data Field Types

    retrieve:
    `GET` the Equipment Data Field Type specified by `name`
    """

    queryset = EQUIPMENT_DATA_FIELD_TYPE_QUERYSET

    serializer_class = EquipmentDataFieldTypeSerializer

    authentication_classes = (
        BasicAuthentication,
        RemoteUserAuthentication,
        SessionAuthentication,
        TokenAuthentication,
    )

    permission_classes = (IsAuthenticatedOrReadOnly,)

    filter_class = EquipmentDataFieldTypeFilter

    ordering_fields = ('name',)

    ordering = ('name',)

    pagination_class = None

    lookup_field = 'name'

    lookup_url_kwarg = 'equipment_data_field_type_name'

    renderer_classes = CoreJSONRenderer, JSONRenderer

    @silk_profile(name='API: Equipment Data Field Types')
    def list(self, request, *args, **kwargs):
        """List items."""
        return super().list(request, *args, **kwargs)

    @silk_profile(name='API: Equipment Data Field Type')
    def retrieve(self, request, *args, **kwargs):
        """Retrieve 1 item."""
        return super().retrieve(request, *args, **kwargs)


class EquipmentGeneralTypeViewSet(ModelViewSet):
    """EquipmentGeneralTypeViewSet.

    list:
    `GET` a filterable, unpaginated list of Equipment General Types

    retrieve:
    `GET` the Equipment General Type specified by `name`

    create:
    `POST` a new Equipment General Type by `name`

    update:
    `PUT` updated data for the Equipment General Type specified by `name`

    partial_update:
    `PATCH` the Equipment General Type specified by `name`

    destroy:
    `DELETE` the Equipment General Type specified by `name`
    """

    queryset = EQUIPMENT_GENERAL_TYPE_QUERYSET

    serializer_class = EquipmentGeneralTypeSerializer

    authentication_classes = (
        BasicAuthentication,
        RemoteUserAuthentication,
        SessionAuthentication,
        TokenAuthentication,
    )

    permission_classes = (IsAuthenticated,)

    filter_class = EquipmentGeneralTypeFilter

    ordering_fields = ('name',)

    ordering = ('name',)

    pagination_class = None

    lookup_field = 'name'

    lookup_url_kwarg = 'equipment_general_type_name'

    renderer_classes = CoreJSONRenderer, JSONRenderer

    @silk_profile(name='API: Equipment General Types')
    def list(self, request, *args, **kwargs):
        """List items."""
        return super().list(request, *args, **kwargs)

    @silk_profile(name='API: Equipment General Type')
    def retrieve(self, request, *args, **kwargs):
        """Retrieve 1 item."""
        return super().retrieve(request, *args, **kwargs)


class EquipmentDataFieldViewSet(ModelViewSet):
    """EquipmentDataFieldViewSet.

    list:
    `GET` a filterable, unpaginated list of Equipment Data Fields

    retrieve:
    `GET` the Equipment Data Field specified by `id`

    create:
    `POST` a new Equipment Data Field

    update:
    `PUT` updated data for the Equipment Data Field specified by `id`

    partial_update:
    `PATCH` the Equipment Data Field specified by `id`

    destroy:
    `DELETE` the Equipment Data Field specified by `id`
    """

    queryset = EQUIPMENT_DATA_FIELD_REST_API_QUERYSET

    serializer_class = EquipmentDataFieldSerializer

    authentication_classes = (
        BasicAuthentication,
        RemoteUserAuthentication,
        SessionAuthentication,
        TokenAuthentication,
    )

    permission_classes = (IsAuthenticated,)

    filter_class = EquipmentDataFieldFilter

    ordering_fields = (
        'equipment_general_type',
        'name',
        'equipment_data_field_type',
        'logical_data_type',
        'numeric_measurement_unit',
    )

    ordering = 'equipment_general_type', 'name'

    pagination_class = None

    renderer_classes = CoreJSONRenderer, JSONRenderer

    @silk_profile(name='API: Equipment Data Fields')
    def list(self, request, *args, **kwargs):
        """List items."""
        return super().list(request, *args, **kwargs)

    @silk_profile(name='API: Equipment Data Field')
    def retrieve(self, request, *args, **kwargs):
        """Retrieve 1 item."""
        return super().retrieve(request, *args, **kwargs)


class EquipmentUniqueTypeGroupViewSet(ModelViewSet):
    """EquipmentUniqueTypeGroupViewSet.

    list:
    `GET` a filterable, unpaginated list of Equipment Unique Type Groups

    retrieve:
    `GET` the Equipment Unique Type Group specified by `name`

    create:
    `POST` a new Equipment Unique Type Group

    update:
    `PUT` updated data for the Equipment Unique Type Group specified by `name`

    partial_update:
    `PATCH` the Equipment Unique Type Group specified by `name`

    destroy:
    `DELETE` the Equipment Unique Type Group specified by `name`
    """

    queryset = EQUIPMENT_UNIQUE_TYPE_GROUP_REST_API_QUERYSET

    serializer_class = EquipmentUniqueTypeGroupSerializer

    authentication_classes = (
        BasicAuthentication,
        RemoteUserAuthentication,
        SessionAuthentication,
        TokenAuthentication,
    )

    permission_classes = (IsAuthenticated,)

    filter_class = EquipmentUniqueTypeGroupFilter

    ordering_fields = 'equipment_general_type', 'name'

    ordering = 'equipment_general_type', 'name'

    pagination_class = None

    lookup_field = 'name'

    lookup_url_kwarg = 'equipment_unique_type_group_name'

    renderer_classes = CoreJSONRenderer, JSONRenderer

    @silk_profile(name='API: Equipment Unique Type Groups')
    def list(self, request, *args, **kwargs):
        """List items."""
        return super().list(request, *args, **kwargs)

    @silk_profile(name='API: Equipment Unique Type Group')
    def retrieve(self, request, *args, **kwargs):
        """Retrieve 1 item."""
        return super().retrieve(request, *args, **kwargs)


class EquipmentUniqueTypeViewSet(ModelViewSet):
    """EquipmentUniqueTypeViewSet.

    list:
    `GET` a filterable, unpaginated list of Equipment Unique Types

    retrieve:
    `GET` the Equipment Unique Type specified by `name`

    create:
    `POST` a new Equipment Unique Type

    update:
    `PUT` updated data for the Equipment Unique Type specified by `name`

    partial_update:
    `PATCH` the Equipment Unique Type specified by `name`

    destroy:
    `DELETE` the Equipment Unique Type specified by `name`
    """

    queryset = EQUIPMENT_UNIQUE_TYPE_REST_API_QUERYSET

    serializer_class = EquipmentUniqueTypeSerializer

    authentication_classes = (
        BasicAuthentication,
        RemoteUserAuthentication,
        SessionAuthentication,
        TokenAuthentication,
    )

    permission_classes = (IsAuthenticated,)

    filter_class = EquipmentUniqueTypeFilter

    ordering_fields = 'equipment_general_type', 'name'

    ordering = 'equipment_general_type', 'name'

    pagination_class = None

    lookup_field = 'name'

    lookup_url_kwarg = 'equipment_unique_type_name'

    renderer_classes = CoreJSONRenderer, JSONRenderer

    @silk_profile(name='API: Equipment Unique Types')
    def list(self, request, *args, **kwargs):
        """List items."""
        return super().list(request, *args, **kwargs)

    @silk_profile(name='API: Equipment Unique Type')
    def retrieve(self, request, *args, **kwargs):
        """Retrieve 1 item."""
        return super().retrieve(request, *args, **kwargs)


class EquipmentFacilityViewSet(ModelViewSet):
    """EquipmentFacilityViewSet.

    list:
    `GET` a filterable, paginated list of Equipment Facilities

    retrieve:
    `GET` the Equipment Facility specified by `name`

    create:
    `POST` a new Equipment Facility

    update:
    `PUT` updated data for the Equipment Facility specified by `name`

    partial_update:
    `PATCH` the Equipment Facility specified by `name`

    destroy:
    `DELETE` the Equipment Facility specified by `name`
    """

    queryset = EQUIPMENT_FACILITY_REST_API_QUERYSET

    serializer_class = EquipmentFacilitySerializer

    authentication_classes = (
        BasicAuthentication,
        RemoteUserAuthentication,
        SessionAuthentication,
        TokenAuthentication,
    )

    permission_classes = (IsAuthenticated,)

    filter_class = EquipmentFacilityFilter

    ordering_fields = ('name',)

    ordering = ('name',)

    pagination_class = LimitOffsetPagination

    lookup_field = 'name'

    lookup_url_kwarg = 'equipment_facility_name'

    renderer_classes = CoreJSONRenderer, JSONRenderer

    @silk_profile(name='API: Equipment Facilities')
    def list(self, request, *args, **kwargs):
        """List items."""
        return super().list(request, *args, **kwargs)

    @silk_profile(name='API: Equipment Facility')
    def retrieve(self, request, *args, **kwargs):
        """Retrieve 1 item."""
        return super().retrieve(request, *args, **kwargs)


class EquipmentInstanceViewSet(ModelViewSet):
    """EquipmentInstanceViewSet.

    list:
    `GET` a filterable, paginated list of Equipment Instances

    retrieve:
    `GET` the Equipment Instance specified by `name`

    create:
    `POST` a new Equipment Instance

    update:
    `PUT` updated data for the Equipment Instance specified by `name`

    partial_update:
    `PATCH` the Equipment Instance specified by `name`

    destroy:
    `DELETE` the Equipment Instance specified by `name`
    """

    queryset = EQUIPMENT_INSTANCE_REST_API_QUERYSET

    serializer_class = EquipmentInstanceSerializer

    authentication_classes = (
        BasicAuthentication,
        RemoteUserAuthentication,
        SessionAuthentication,
        TokenAuthentication,
    )

    permission_classes = (IsAuthenticated,)

    filter_class = EquipmentInstanceFilter

    ordering_fields = (
        'equipment_general_type',
        'equipment_unique_type',
        'name',
        'equipment_facility',
    )

    ordering = 'equipment_general_type', 'equipment_unique_type', 'name'

    lookup_field = 'name'

    lookup_url_kwarg = 'equipment_instance_name'

    pagination_class = LimitOffsetPagination

    renderer_classes = CoreJSONRenderer, JSONRenderer

    @silk_profile(name='API: Equipment Instances')
    def list(self, request, *args, **kwargs):
        """List items."""
        return super().list(request, *args, **kwargs)

    @silk_profile(name='API: Equipment Instance')
    def retrieve(self, request, *args, **kwargs):
        """Retrieve 1 item."""
        return super().retrieve(request, *args, **kwargs)


class EquipmentSystemViewSet(ModelViewSet):
    """EquipmentSystemViewSet.

    list:
    `GET` a filterable, paginated list of Equipment Systems

    retrieve:
    `GET` the Equipment System specified by `id`

    create:
    `POST` a new Equipment System

    update:
    `PUT` updated data for the Equipment System specified by `id`

    partial_update:
    `PATCH` the Equipment System specified by `id`

    destroy:
    `DELETE` the Equipment System specified by `id`
    """

    queryset = EQUIPMENT_SYSTEM_REST_API_QUERYSET

    serializer_class = EquipmentSystemSerializer

    authentication_classes = (
        BasicAuthentication,
        RemoteUserAuthentication,
        SessionAuthentication,
        TokenAuthentication,
    )

    permission_classes = (IsAuthenticated,)

    filter_class = EquipmentSystemFilter

    ordering_fields = 'equipment_facility', 'name', 'date'

    ordering = 'equipment_facility', 'name', 'date'

    pagination_class = LimitOffsetPagination

    renderer_classes = CoreJSONRenderer, JSONRenderer

    @silk_profile(name='API: Equipment Systems')
    def list(self, request, *args, **kwargs):
        """List items."""
        return super().list(request, *args, **kwargs)

    @silk_profile(name='API: Equipment System')
    def retrieve(self, request, *args, **kwargs):
        """Retrieve 1 item."""
        return super().retrieve(request, *args, **kwargs)
