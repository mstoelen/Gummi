// Generated by gencpp from file pr2_msgs/GPUStatus.msg
// DO NOT EDIT!


#ifndef PR2_MSGS_MESSAGE_GPUSTATUS_H
#define PR2_MSGS_MESSAGE_GPUSTATUS_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace pr2_msgs
{
template <class ContainerAllocator>
struct GPUStatus_
{
  typedef GPUStatus_<ContainerAllocator> Type;

  GPUStatus_()
    : header()
    , product_name()
    , pci_device_id()
    , pci_location()
    , display()
    , driver_version()
    , temperature(0.0)
    , fan_speed(0.0)
    , gpu_usage(0.0)
    , memory_usage(0.0)  {
    }
  GPUStatus_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , product_name(_alloc)
    , pci_device_id(_alloc)
    , pci_location(_alloc)
    , display(_alloc)
    , driver_version(_alloc)
    , temperature(0.0)
    , fan_speed(0.0)
    , gpu_usage(0.0)
    , memory_usage(0.0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _product_name_type;
  _product_name_type product_name;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _pci_device_id_type;
  _pci_device_id_type pci_device_id;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _pci_location_type;
  _pci_location_type pci_location;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _display_type;
  _display_type display;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _driver_version_type;
  _driver_version_type driver_version;

   typedef float _temperature_type;
  _temperature_type temperature;

   typedef float _fan_speed_type;
  _fan_speed_type fan_speed;

   typedef float _gpu_usage_type;
  _gpu_usage_type gpu_usage;

   typedef float _memory_usage_type;
  _memory_usage_type memory_usage;




  typedef boost::shared_ptr< ::pr2_msgs::GPUStatus_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pr2_msgs::GPUStatus_<ContainerAllocator> const> ConstPtr;

}; // struct GPUStatus_

typedef ::pr2_msgs::GPUStatus_<std::allocator<void> > GPUStatus;

typedef boost::shared_ptr< ::pr2_msgs::GPUStatus > GPUStatusPtr;
typedef boost::shared_ptr< ::pr2_msgs::GPUStatus const> GPUStatusConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::pr2_msgs::GPUStatus_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::pr2_msgs::GPUStatus_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace pr2_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'pr2_msgs': ['/home/joe/repos/GummiArm/orchestration/packages/src/pr2_common/pr2_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::pr2_msgs::GPUStatus_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pr2_msgs::GPUStatus_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pr2_msgs::GPUStatus_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pr2_msgs::GPUStatus_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pr2_msgs::GPUStatus_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pr2_msgs::GPUStatus_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::pr2_msgs::GPUStatus_<ContainerAllocator> >
{
  static const char* value()
  {
    return "4c74e5474b8aade04e56108262099c6e";
  }

  static const char* value(const ::pr2_msgs::GPUStatus_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x4c74e5474b8aade0ULL;
  static const uint64_t static_value2 = 0x4e56108262099c6eULL;
};

template<class ContainerAllocator>
struct DataType< ::pr2_msgs::GPUStatus_<ContainerAllocator> >
{
  static const char* value()
  {
    return "pr2_msgs/GPUStatus";
  }

  static const char* value(const ::pr2_msgs::GPUStatus_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::pr2_msgs::GPUStatus_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n\
string product_name\n\
string pci_device_id\n\
string pci_location\n\
string display\n\
string driver_version\n\
float32 temperature # Temperature in Celcius\n\
float32 fan_speed # Fan speed in rad/s\n\
float32 gpu_usage # Usage in percent\n\
float32 memory_usage # Usage in percent\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
";
  }

  static const char* value(const ::pr2_msgs::GPUStatus_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::pr2_msgs::GPUStatus_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.product_name);
      stream.next(m.pci_device_id);
      stream.next(m.pci_location);
      stream.next(m.display);
      stream.next(m.driver_version);
      stream.next(m.temperature);
      stream.next(m.fan_speed);
      stream.next(m.gpu_usage);
      stream.next(m.memory_usage);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct GPUStatus_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::pr2_msgs::GPUStatus_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::pr2_msgs::GPUStatus_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "product_name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.product_name);
    s << indent << "pci_device_id: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.pci_device_id);
    s << indent << "pci_location: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.pci_location);
    s << indent << "display: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.display);
    s << indent << "driver_version: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.driver_version);
    s << indent << "temperature: ";
    Printer<float>::stream(s, indent + "  ", v.temperature);
    s << indent << "fan_speed: ";
    Printer<float>::stream(s, indent + "  ", v.fan_speed);
    s << indent << "gpu_usage: ";
    Printer<float>::stream(s, indent + "  ", v.gpu_usage);
    s << indent << "memory_usage: ";
    Printer<float>::stream(s, indent + "  ", v.memory_usage);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PR2_MSGS_MESSAGE_GPUSTATUS_H
