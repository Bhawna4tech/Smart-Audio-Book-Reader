
  import button
import press_up
import press_down
import press_left
import press_right
import rpi_shutdown
import global_var


  def update_read(self):
        print "str1"
        button.one()
	self.parent.after(100 , self.update_read)

    def x2(self):
        print "str2"
	press_up.button_up()
	self.parent.after(100 , self.x2)

    def x3(self):
        print "str2"
	press_down.button_down()
	self.parent.after(100 , self.x3)

	#press_left.button_left()
	#press_right.button_right()
#	rpi_shutdown.shut_down()
	