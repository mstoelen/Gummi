#!/usr/bin/env python
# -­*­- coding: utf-8 ­-*-­

from threading import Lock
import wx
import csv
import sys
import random, codecs
import time
from math import pi

import rospy
from sensor_msgs.msg import JointState


class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        self.gui_available = False  # True when the GUI object is available
        self.received = False  # True when the first joint_states were received

	self.gui_lock = Lock()

        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, (1400,700))
        panel = wx.Panel(self, -1)

        self.jointStatePub = rospy.Publisher("gummi/joint_commands", JointState,  queue_size=10)
        self.suscribe = rospy.Subscriber('gummi/joint_states', JointState, self.cmdCallback)

        lastbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hboxc = wx.BoxSizer(wx.HORIZONTAL)
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        vbox3 = wx.BoxSizer(wx.VERTICAL)
        vbox4 = wx.BoxSizer(wx.VERTICAL)
        vbox5 = wx.BoxSizer(wx.VERTICAL)
        vbox6 = wx.BoxSizer(wx.VERTICAL)
        vbox7 = wx.BoxSizer(wx.VERTICAL)
        vbox8 = wx.BoxSizer(wx.VERTICAL)

        name1 = "Shoulder yaw"
        name2 = "Shoulder roll"
        name3 = "Shoulder pitch"
        name4 = "Upper arm roll"
        name5 = "Elbow"
        name6 = "Forearm"
        name7 = "Wrist"
        name8 = "Hand DOF1"

        self.jointNames = ("shoulder_yaw", "shoulder_roll", "shoulder_pitch", "upperarm_roll", "elbow", "forearm_roll", "wrist_pitch", "hand_dof1")
        self.encoder_position = dict(zip(self.jointNames,[None]*len(self.jointNames)))
        self.encoder_effort = dict(zip(self.jointNames,[None]*len(self.jointNames)))

        rospy.init_node('GummiHMI', anonymous=False, disable_signals=True)
        self.r = rospy.Rate(60)

        # text_a = wx.StaticText(panel, label= "Joint angle", pos= wx.DefaultPosition)
        # text_c = wx.StaticText(panel, label= "Co-contraction", pos= wx.DefaultPosition)

        text1 = wx.StaticText(panel, label= name1, pos= wx.DefaultPosition)
        text2 = wx.StaticText(panel, label= name2, pos= wx.DefaultPosition)
        text3 = wx.StaticText(panel, label= name3, pos= wx.DefaultPosition)
        text4 = wx.StaticText(panel, label= name4, pos= wx.DefaultPosition)
        text5 = wx.StaticText(panel, label= name5, pos= wx.DefaultPosition)
        text6 = wx.StaticText(panel, label= name6, pos= wx.DefaultPosition)
        text7 = wx.StaticText(panel, label= name7, pos= wx.DefaultPosition)
        text8 = wx.StaticText(panel, label= name8, pos= wx.DefaultPosition)

        self.sld = wx.Slider(panel, value = 0* (180/pi), minValue = rospy.get_param("~shoulder_yaw/minAngle") * (180/pi), maxValue = rospy.get_param("~shoulder_yaw/maxAngle") * (180/pi), pos = wx.DefaultPosition, size = (150, -1),
                              style = wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)

        self.sld2 = wx.Slider(panel, value = 0* (180/pi), minValue = rospy.get_param("~shoulder_roll/minAngle")* (180/pi), maxValue = rospy.get_param("~shoulder_roll/maxAngle")* (180/pi), pos = wx.DefaultPosition, size = (150, -1),
                              style = wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)

        self.sld3 = wx.Slider(panel, value = 0* (180/pi), minValue = rospy.get_param("~shoulder_pitch/minAngle")* (180/pi), maxValue = rospy.get_param("~shoulder_pitch/maxAngle") * (180/pi), pos = wx.DefaultPosition, size = (150, -1),
                              style = wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)

        self.sld4 = wx.Slider(panel, value = 0* (180/pi), minValue = - (pi/2) *  (180/pi), maxValue = (pi/2) * (180/pi), pos = wx.DefaultPosition, size = (150, -1),
                              style = wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)

        self.sld5 = wx.Slider(panel, value = 0* (180/pi), minValue = rospy.get_param("~elbow/minAngle")* (180/pi), maxValue = rospy.get_param("~elbow/maxAngle")* (180/pi), pos = wx.DefaultPosition, size = (150, -1),
                              style = wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)

        self.sld6 = wx.Slider(panel, value = 0* (180/pi), minValue = -1.75/2*pi* (180/pi), maxValue = 1.75/2*pi* (180/pi), pos = wx.DefaultPosition, size = (150, -1),
                              style = wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)

        self.sld7 = wx.Slider(panel, value = 0* (180/pi), minValue = rospy.get_param("~wrist/minAngle")* (180/pi), maxValue = rospy.get_param("~wrist/maxAngle") * (180/pi), pos = wx.DefaultPosition, size = (150, -1),
                              style = wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)

        self.sld8 = wx.Slider(panel, value = 0* (180/pi), minValue = -1.75/2*pi* (180/pi), maxValue = 1.75/2*pi* (180/pi), pos = wx.DefaultPosition, size = (150, -1),
                              style = wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)

        self.sldc = wx.Slider(panel, value = 30, minValue = 1, maxValue = 100, pos = wx.DefaultPosition, size = (150, -1),
                              style = wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)

        self.sld2c = wx.Slider(panel, value = 30, minValue = 1, maxValue = 100, pos = wx.DefaultPosition, size = (150, -1),
                              style = wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)
        self.sld3c = wx.Slider(panel, value = 30, minValue = 1, maxValue = 100, pos = wx.DefaultPosition, size = (150, -1),
                              style = wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)
        self.sld4c = wx.Slider(panel, value = 30, minValue = 1, maxValue = 100, pos = wx.DefaultPosition, size = (150, -1),
                              style = wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)
        self.sld5c = wx.Slider(panel, value = 60, minValue = 1, maxValue = 100, pos = wx.DefaultPosition, size = (150, -1),
                              style = wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)

        self.sld.Bind(wx.EVT_SCROLL, self.OnSliderScroll)
        self.sld2.Bind(wx.EVT_SCROLL, self.OnSliderScroll)
        self.sld3.Bind(wx.EVT_SCROLL, self.OnSliderScroll)
        self.sld4.Bind(wx.EVT_SCROLL, self.OnSliderScroll)
        self.sld5.Bind(wx.EVT_SCROLL, self.OnSliderScroll)
        self.sld6.Bind(wx.EVT_SCROLL, self.OnSliderScroll)
        self.sld7.Bind(wx.EVT_SCROLL, self.OnSliderScroll)
        self.sld8.Bind(wx.EVT_SCROLL, self.OnSliderScroll)

        self.sldc.Bind(wx.EVT_SCROLL, self.OnSliderScroll)
        self.sld2c.Bind(wx.EVT_SCROLL, self.OnSliderScroll)
        self.sld3c.Bind(wx.EVT_SCROLL, self.OnSliderScroll)
        self.sld4c.Bind(wx.EVT_SCROLL, self.OnSliderScroll)
        self.sld5c.Bind(wx.EVT_SCROLL, self.OnSliderScroll)

        vbox1.Add(text1,1 , wx.ALIGN_CENTRE)
        vbox1.Add(self.sld, 1 , wx.ALIGN_CENTRE)
        vbox1.Add(wx.StaticText(panel, label= "Joint angle", pos= wx.DefaultPosition),1 , wx.ALIGN_CENTRE)
        vbox1.Add(self.sldc, 1 , wx.ALIGN_CENTRE)
        vbox1.Add(wx.StaticText(panel, label= "Co-contraction", pos= wx.DefaultPosition), 1 , wx.ALIGN_CENTRE)

        vbox2.Add(text2,1 , wx.ALIGN_CENTRE)
        vbox2.Add(self.sld2, 1 , wx.ALIGN_CENTRE)
        vbox2.Add(wx.StaticText(panel, label= "Joint angle", pos= wx.DefaultPosition),1 , wx.ALIGN_CENTRE)
        vbox2.Add(self.sld2c, 1 , wx.ALIGN_CENTRE)
        vbox2.Add(wx.StaticText(panel, label= "Co-contraction", pos= wx.DefaultPosition), 1 , wx.ALIGN_CENTRE)

        vbox3.Add(text3,1 , wx.ALIGN_CENTRE)
        vbox3.Add(self.sld3, 1 , wx.ALIGN_CENTRE)
        vbox3.Add(wx.StaticText(panel, label= "Joint angle", pos= wx.DefaultPosition),1 , wx.ALIGN_CENTRE)
        vbox3.Add(self.sld3c, 1 , wx.ALIGN_CENTRE)
        vbox3.Add(wx.StaticText(panel, label= "Co-contraction", pos= wx.DefaultPosition), 1 , wx.ALIGN_CENTRE)

        vbox4.Add(text4,1 , wx.ALIGN_CENTRE)
        vbox4.Add(self.sld4, 1 , wx.ALIGN_CENTRE)
        vbox4.Add(wx.StaticText(panel, label= "Joint angle", pos= wx.DefaultPosition),1 , wx.ALIGN_CENTRE)

        vbox5.Add(text5,1 , wx.ALIGN_CENTRE)
        vbox5.Add(self.sld5, 1 , wx.ALIGN_CENTRE)
        vbox5.Add(wx.StaticText(panel, label= "Joint angle", pos= wx.DefaultPosition),1 , wx.ALIGN_CENTRE)
        vbox5.Add(self.sld4c, 1 , wx.ALIGN_CENTRE)
        vbox5.Add(wx.StaticText(panel, label= "Co-contraction", pos= wx.DefaultPosition), 1 , wx.ALIGN_CENTRE)

        vbox6.Add(text6,1 , wx.ALIGN_CENTRE)
        vbox6.Add(self.sld6, 1 , wx.ALIGN_CENTRE)
        vbox6.Add(wx.StaticText(panel, label= "Joint angle", pos= wx.DefaultPosition),1 , wx.ALIGN_CENTRE)

        vbox7.Add(text7,1 , wx.ALIGN_CENTRE)
        vbox7.Add(self.sld7, 1 , wx.ALIGN_CENTRE)
        vbox7.Add(wx.StaticText(panel, label= "Joint angle", pos= wx.DefaultPosition),1 , wx.ALIGN_CENTRE)
        vbox7.Add(self.sld5c, 1 , wx.ALIGN_CENTRE)
        vbox7.Add(wx.StaticText(panel, label= "Co-contraction", pos= wx.DefaultPosition), 1 , wx.ALIGN_CENTRE)

        vbox8.Add(text8,1 , wx.ALIGN_CENTRE)
        vbox8.Add(self.sld8, 1 , wx.ALIGN_CENTRE)
        vbox8.Add(wx.StaticText(panel, label= "Joint angle", pos= wx.DefaultPosition),1 , wx.ALIGN_CENTRE)

        cb1 = wx.CheckBox(panel, label = 'Passive', pos = wx.DefaultPosition)
        cb1.Bind(wx.EVT_CHECKBOX,self.onChecked)

        btn1 = wx.Button(panel, 12, 'Save')
        wx.EVT_BUTTON(self, 12, self.OnSave)

        hbox.Add(vbox1, 1 , wx.ALIGN_CENTRE)
        hbox.Add(vbox2, 1 , wx.ALIGN_CENTRE)
        hbox.Add(vbox3, 1 , wx.ALIGN_CENTRE)
        hbox.Add(vbox4, 1 , wx.ALIGN_CENTRE)

        self.textFile = wx.TextCtrl(panel, size=(140, -1), value='out.csv')

        hbox.Add(vbox5, 1 , wx.ALIGN_CENTRE)
        hbox.Add(vbox6, 1 , wx.ALIGN_CENTRE)
        hbox.Add(vbox7, 1 , wx.ALIGN_CENTRE)
        hbox.Add(vbox8, 1 , wx.ALIGN_CENTRE)

        lastbox.Add(hbox, 1 , wx.ALIGN_CENTRE)
        lastbox.Add(hboxc, 1 , wx.ALIGN_TOP)
        lastbox.Add(btn1, 0 ,wx.ALIGN_CENTRE |wx.ALL, 10)
        lastbox.Add(self.textFile, 0 ,wx.ALIGN_LEFT |wx.ALL, 10)

        panel.SetSizer(lastbox)
        lastbox.Fit(panel)

        self.sld.Enable(False)
        self.sld2.Enable(False)
        self.sld3.Enable(False)
        self.sld4.Enable(False)
        self.sld5.Enable(False)
        self.sld6.Enable(False)
        self.sld7.Enable(False)
        self.sld8.Enable(False)

        self.sldc.Enable(False)
        self.sld2c.Enable(False)
        self.sld3c.Enable(False)
        self.sld4c.Enable(False)
        self.sld5c.Enable(False)

        self.gui_available = True

    def onChecked(self, e):
        cb = e.GetEventObject()
        if cb.GetValue():
            self.sld.Enable(False)
            self.sld2.Enable(False)
            self.sld3.Enable(False)
            self.sld4.Enable(False)
            self.sld5.Enable(False)
            self.sld6.Enable(False)
            self.sld7.Enable(False)
            self.sld8.Enable(False)

            self.sldc.Enable(False)
            self.sld2c.Enable(False)
            self.sld3c.Enable(False)
            self.sld4c.Enable(False)
            self.sld5c.Enable(False)

            self.sendCommand(False)
        else:
            self.sld.Enable(True)
            self.sld2.Enable(True)
            self.sld3.Enable(True)
            self.sld4.Enable(True)
            self.sld5.Enable(True)
            self.sld6.Enable(True)
            self.sld7.Enable(True)
            self.sld8.Enable(True)

            self.sldc.Enable(True)
            self.sld2c.Enable(True)
            self.sld3c.Enable(True)
            self.sld4c.Enable(True)
            self.sld5c.Enable(True)

            self.sendCommand(True)


    def OnSave(self,evt) :
       fileName = self.textFile.GetValue()
       with open(fileName, 'wb') as csvfile:
           writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
           writer.writerow([self.sld.GetValue()*(pi/180.0),self.sld2.GetValue()*(pi/180.0),self.sld3.GetValue()*(pi/180.0),self.sld4.GetValue()*(pi/180.0),self.sld5.GetValue()*(pi/180.0),self.sld6.GetValue()*(pi/180.0),self.sld7.GetValue()*(pi/180.0),self.sld8.GetValue()*(pi/180.0)])

    def OnSliderScroll(self,evt) :
        self.sendCommand(True)

    def sendCommand(self, active):
      if self.received:
          if active:
              sign = 1
          else:
              sign = -1
          current_position = [self.sld.GetValue()*(pi/180.0),self.sld2.GetValue()*(pi/180.0),self.sld3.GetValue()*(pi/180.0),self.sld4.GetValue()*(pi/180.0),self.sld5.GetValue()*(pi/180.0),self.sld6.GetValue()*(pi/180.0),self.sld7.GetValue()*(pi/180.0),self.sld8.GetValue()*(pi/180.0)]
          msg = JointState()
          msg.header.stamp = rospy.Time.now()
          msg.position = current_position
          msg.name = self.jointNames
          msg.effort = [sign*self.sldc.GetValue()/100.0,sign*self.sld2c.GetValue()/100.0,sign*self.sld3c.GetValue()/100.0,0,sign*self.sld4c.GetValue()/100.0,0,sign*self.sld5c.GetValue()/100.0]

	  with self.gui_lock:
	  	self.jointStatePub.publish(msg)
          	self.r.sleep()


    def cmdCallback(self, msg):
      if self.gui_available:
        for name,pos,eff in zip(msg.name,msg.position,msg.effort):
              self.encoder_position[name] = pos
              self.encoder_effort[name] = eff

    	with self.gui_lock:
            # Considering the jointNames are these ones:
            # ("shoulder_yaw", "shoulder_roll", "shoulder_pitch", "upperarm_roll", "elbow", "forearm_roll", "wrist_pitch", "hand_dof1")
            self.sld.SetValue(int(self.encoder_position[self.jointNames[0]]/(pi/180.0)))
            self.sld2.SetValue(int(self.encoder_position[self.jointNames[1]]/(pi/180.0)))
            self.sld3.SetValue(int(self.encoder_position[self.jointNames[2]]/(pi/180.0)))
            self.sld4.SetValue(int(self.encoder_position[self.jointNames[3]]/(pi/180.0)))
            self.sld5.SetValue(int(self.encoder_position[self.jointNames[4]]/(pi/180.0)))
            self.sld6.SetValue(int(self.encoder_position[self.jointNames[5]]/(pi/180.0)))
            self.sld7.SetValue(int(self.encoder_position[self.jointNames[6]]/(pi/180.0)))
            self.sld8.SetValue(int(self.encoder_position[self.jointNames[7]]/(pi/180.0)))

            self.sldc.SetValue(int(100*self.encoder_effort[self.jointNames[0]]))
            self.sld2c.SetValue(int(100*self.encoder_effort[self.jointNames[1]]))
            self.sld3c.SetValue(int(100*self.encoder_effort[self.jointNames[2]]))
            self.sld4c.SetValue(int(100*self.encoder_effort[self.jointNames[4]]))
            self.sld5c.SetValue(int(100*self.encoder_effort[self.jointNames[6]]))

        if not self.received:
            self.sld.Enable(True)
            self.sld2.Enable(True)
            self.sld3.Enable(True)
            self.sld4.Enable(True)
            self.sld5.Enable(True)
            self.sld6.Enable(True)
            self.sld7.Enable(True)
            self.sld8.Enable(True)
            self.sldc.Enable(True)
            self.sld2c.Enable(True)
            self.sld3c.Enable(True)
            self.sld5c.Enable(True)
            self.sld4c.Enable(True)

            self.received = True


class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, 'slider.py')
        frame.Show(True)
        frame.Centre()

	# This was necessary because the wx object was killed, but ROS would try to call cmdCallback
	def on_end_session(e):
	    rospy.signal_shutdown("wx window closed")
	    e.Skip()

	frame.Bind(wx.EVT_END_SESSION, on_end_session)

	frame.Bind(wx.EVT_CLOSE, on_end_session)

        #while not rospy.is_shutdown():
        #    frame.r.sleep()

        return True

app = MyApp(0)
app.MainLoop()
