
$(document).ready(function () {

    console.log("i am here external js");
    document.getElementsByName('designationOptions').forEach(radio => {
        if(radio.checked)
        {
           $faculty_designation=radio.value;
           console.log($faculty_designation);
        }
    });

    //add class form clicking

    // Data Picker Initialization
    // $('.datepicker').pickadate();

    //add-faculty-btnId 
    $('#add-faculty-btnId').on('click',function()
    {
         console.log('add faculty  clicked');
         document.getElementsByName('designationOptions').forEach(radio => {
            if(radio.checked)
            {
               $faculty_designation=radio.value;
               console.log($faculty_designation);
            }
        });
         $faculty_name=$('#faculty-nameId').val();

         if($faculty_designation=='' || $faculty_name=='')
         {
            alert('all feild should be filled.')
         }
         else
         {
            $.ajax(
                {
                    type: 'POST',
                    url: 'insertfaculty',
                    data:
                    {
                        faculty_name:$faculty_name,
                        faculty_designation:$faculty_designation,
                        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                    },
                    success: function () {
                        alert('data saved');
                        $('#faculty-nameId').val('');
                        window.location = "/";
                    }
                }
            )
         }
    });


    //class submit button clicked
    $('#submit-class-btnId').on('click', function () {

        console.log('submit button clicked.');

        $semester = $('#semesterId').text();
        $courseCode = $('#courseCodeId').text();
        $courseName = $('#courseNameId').text();
        $teacher = $('#assignedTeacherId').text();
        $classRoom = $('#classRoomId').text();
        $classDate = $('#class-date').val();
        $classTime = $('#class-time').val();
        $duration = $('#durationId').text();

        console.log($semester);
        console.log($courseCode);
        console.log($courseName);
        console.log($teacher);
        console.log($classRoom);
        console.log($classDate);
        console.log($classTime);
        console.log($duration);


        if ($classRoom == "" || $classTime == "" || $courseCode == "" ||
            $courseName == "" || $duration == "" || $semester == "" || $teacher == "") {
            //console.log($classTime);
            alert("please complete all Fields")
        }
        else {




            $.ajax(
                {
                    type: 'POST',
                    url: 'insert',
                    data:
                    {
                        semester: $semester,
                        courseCode: $courseCode,
                        courseName: $courseName,
                        teacher: $teacher,
                        classRoom: $classRoom,
                        classDate: $classDate,
                        classTime: $classTime,
                        duration: $duration,
                        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                    },
                    success: function () {
                        alert('data saved');
                        $('#semesterId').text('');
                        $('#courseCodeId').text('');
                        $('#courseNameId').text('');
                        $('#assignedTeacherId').text('');
                        $('#classRoomId').text('');
                        $('#class-date').val('');
                        $('#class-time').val('');
                        $('#durationId').text('');
                        window.location = "/";
                    }
                }
            )
        }

    });

    //add notice button clicked
    $('#add-notice-btnId').on('click',function()
    {
          $notice_title=$('#noticetitleId').val();
          $notice_description=$('#noticedescriptionId').val();

          if($notice_title=="" ||$notice_description=="")
          {
              alert('all need to be filled...');
          }
          else{

            $.ajax(
                {
                    type: 'POST',
                    url: 'insertnotice',
                    data:
                    {
                        notice_title:$notice_title,
                        notice_description:$notice_description,
                        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                    },
                    success: function () {
                        alert('data saved');
                        $('#noticedescriptionId').val('');
                        $('#noticetitleId').val('');
                        window.location = "/";
                    }
                }
            )
          }
    });


    //clicking the dropdowns
    //select semester clicked
    $('.semester-item').click(function () {
        $('#semesterId').text($(this).text());
        console.log($(this).text());
    });

    //select course code clicked
    $('.course-code-item').click(function () {
        $('#courseCodeId').text($(this).text());
        console.log($(this).text());
    });

    //select course name clicked
    $('.course-name-item').click(function () {
        $('#courseNameId').text($(this).text());
        console.log($(this).text());
    });

    //select teacher clicked
    $('.teacher-item').click(function () {
        $('#assignedTeacherId').text($(this).text());
        console.log($(this).text());
    });

    //select classroom clicked
    $('.classroom-item').click(function () {
        $('#classRoomId').text($(this).text());
        console.log($(this).text());
    });
    // class duraion
    $('.duration-item').click(function () {
        $('#durationId').text($(this).text());
        console.log($(this).text());
    });


});
