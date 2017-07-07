// Generated by gencpp from file pr2_msgs/PowerState.msg
// DO NOT EDIT!


#ifndef PR2_MSGS_MESSAGE_POWERSTATE_H
#define PR2_MSGS_MESSAGE_POWERSTATE_H


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
struct PowerState_
{
  typedef PowerState_<ContainerAllocator> Type;

  PowerState_()
    : header()
    , power_consumption(0.0)
    , time_remaining()
    , prediction_method()
    , relative_capacity(0)
    , AC_present(0)  {
    }
  PowerState_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , power_consumption(0.0)
    , time_remaining()
    , prediction_method(_alloc)
    , relative_capacity(0)
    , AC_present(0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef double _power_consumption_type;
  _power_consumption_type power_consumption;

   typedef ros::Duration _time_remaining_type;
  _time_remaining_type time_remaining;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _prediction_method_type;
  _prediction_method_type prediction_method;

   typedef int8_t _relative_capacity_type;
  _relative_capacity_type relative_capacity;

   typedef int8_t _AC_present_type;
  _AC_present_type AC_present;




  typedef boost::shared_ptr< ::pr2_msgs::PowerState_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pr2_msgs::PowerState_<ContainerAllocator> const> ConstPtr;

}; // struct PowerState_

typedef ::pr2_msgs::PowerState_<std::allocator<void> > PowerState;

typedef boost::shared_ptr< ::pr2_msgs::PowerState > PowerStatePtr;
typedef boost::shared_ptr< ::pr2_msgs::PowerState const> PowerStateConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::pr2_msgs::PowerState_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::pr2_msgs::PowerState_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::pr2_msgs::PowerState_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pr2_msgs::PowerState_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pr2_msgs::PowerState_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pr2_msgs::PowerState_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pr2_msgs::PowerState_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pr2_msgs::PowerState_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::pr2_msgs::PowerState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "e6fa46a387cad0b7a80959a21587a6c9";
  }

  static const char* value(const ::pr2_msgs::PowerState_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xe6fa46a387cad0b7ULL;
  static const uint64_t static_value2 = 0xa80959a21587a6c9ULL;
};

template<class ContainerAllocator>
struct DataType< ::pr2_msgs::PowerState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "pr2_msgs/PowerState";
  }

  static const char* value(const ::pr2_msgs::PowerState_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::pr2_msgs::PowerState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# This message communicates the state of the PR2's power system.\n\
Header header\n\
float64 power_consumption ## Watts\n\
duration time_remaining ## estimated time to empty or full\n\
string prediction_method ## how time_remaining is being calculated\n\
int8  relative_capacity ## percent of capacity\n\
int8  AC_present ## number of packs detecting AC power, > 0 means plugged in\n\
\n\
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

  static const char* value(const ::pr2_msgs::PowerState_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::pr2_msgs::PowerState_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.power_consumption);
      stream.next(m.time_remaining);
      stream.next(m.prediction_method);
      stream.next(m.relative_capacity);
      stream.next(m.AC_present);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct PowerState_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::pr2_msgs::PowerState_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::pr2_msgs::PowerState_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "power_consumption: ";
    Printer<double>::stream(s, indent + "  ", v.power_consumption);
    s << indent << "time_remaining: ";
    Printer<ros::Duration>::stream(s, indent + "  ", v.time_remaining);
    s << indent << "prediction_method: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.prediction_method);
    s << indent << "relative_capacity: ";
    Printer<int8_t>::stream(s, indent + "  ", v.relative_capacity);
    s << indent << "AC_present: ";
    Printer<int8_t>::stream(s, indent + "  ", v.AC_present);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PR2_MSGS_MESSAGE_POWERSTATE_H
