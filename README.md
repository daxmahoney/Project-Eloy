Thank you for the opportunity to write my first Python program. The solution I have 
provided uses absolute positioning to return the output objects you desired. 

To run my solution you should open the terminal window on your UNIX based computer and type the following commands. I will assume you are able to navigate to the location where you downloaded the code I submitted.

1. '$pip3 install json'
2. navigate to the folder where you cloned the repository I have provided
3. '$python refactor.py'
4. '$cat testfile.txt'




***# HL7 translation exercise

In this exercise, you'll be required to extract data from raw HL7 messages and produce normalized output objects that could be consumed by downstream systems.

HL7 is a standard used to share patient data between hospital systems. Each HL7 message consists of multiple segments, with carriage return characters (`\r`) used as a delimiter. Each segment is further divided using pipe characters (`|`) to separate fields, with the first field containing an identifier for the type of segment. Particular data elements can be identified using the position of a field within a type of segment. It is also possible to subdivide fields using a caret character (`^`).

The `messages.ldjson` input file contains 10 JSON-encoded message objects, each on its own line. Message objects contain metadata as well as the raw message text, which is identified by the `text` key. Process the text for every message to extract each observation and append an event to your output with the required attributes.

Each output line corresponds to an `OBX` line in the original message and describes an individual observation of the patient. The `OBR` line in the message contains data pertaining to all subsequent `OBX` lines, so some fields will be repeated in each output line. The patient can be identified using a field in the `PID` line.

Note that message lines displayed in this document are separated by newline characters (`\n`) to make things easier to read, while segments in the real messages are separated by carriage return characters (`\r`).


## The problem

Something about markdown:
I believe the 'pre' tag has to be separated from the block of HTML code by a line, otherwise '**' can be used for inline emphasis
I would dispense with the emphasis altogether as it differs from the messages contained in the file you provide, and would be something that is asked about over and over again
Otherwise I would say "emphasis added to the important bits"

Given a JSON-encoded object containing this message:

<pre>

MSH|^~\\&|HL7|VITALS|EXAMPLE HOSPITAL||201701120900||ORU^R01|53b3cd1ea11b448ebf99656f637e54e3|P|2.3||||||UNICODE UTF-8
PID|||**40724907**^^^A^MR||
PV1||E|STIC^STIC^01^^^^EXAMPLE HOSPITAL
OBR|1||||||**20170112000800**
OBX|1|ST|^**SBP**^^8480-6^Systolic blood pressure^LN||**154**|**mm(hg)**||R
OBX|2|ST|^**HR**^^8886-4^Heart rate^LN||**99**|**beats/min**||R
OBX|3||^**MBP**^^8478-0^Mean blood pressure^LN||**120**|**mm(hg)**||R
OBX|4|ST|^**CVP3**^^8591-0^Central venous pressure (CVP) Mean^LN||**13**|**mm(hg)**||R
OBX|5|ST|^**DBP**^^8462-4^Diastolic blood pressure^LN||**103**|**mm(hg)**||R
OBX|6|ST|^**SPO2-%**^^20081-6^Pulse oximetry site^LN||**96**|**%**||R
OBX|7|ST|^**RR**^^9279-1^Respiratory rate^LN||**16**|**breaths/min**||R

</pre>

Produce this output:

    {"event":"SBP","patient":"40724907","time":"2017-01-12T00:08:00Z","unit":"mm(hg)","value":154}
    {"event":"HR","patient":"40724907","time":"2017-01-12T00:08:00Z","unit":"beats/min","value":99}
    {"event":"MBP","patient":"40724907","time":"2017-01-12T00:08:00Z","unit":"mm(hg)","value":120}
    {"event":"CVP3","patient":"40724907","time":"2017-01-12T00:08:00Z","unit":"mm(hg)","value":13}
    {"event":"DBP","patient":"40724907","time":"2017-01-12T00:08:00Z","unit":"mm(hg)","value":103}
    {"event":"SPO2-%","patient":"40724907","time":"2017-01-12T00:08:00Z","unit":"%","value":96}
    {"event":"RR","patient":"40724907","time":"2017-01-12T00:08:00Z","unit":"breaths/min","value":16}


## The solution

Each JSON-encoded output object must be written to a single line, with each line separated by a newline (`\n`) character. It's acceptable to include blank lines in your output, as well as comment lines with a leading `#` character.

For the purposes of this exercise, it's safe to make the following assumptions:

  * The message text encoding is UTF-8
  * All times are in UTC
  * Messages will only contain one `OBR` segment
  * All required values will be present in the message

Your output objects must have the following fields:

  * `event` is a a string identifying the kind of observation
  * `patient` is an 8-digit string that uniquely identifies a patient
  * `time` is a string containing the ISO8601-encoded time when the observation occurred
  * `unit` is a string containing the relevant unit of measure
  * `value` is an integer containing an observed measurement

Save your work in a clone of this repository. You aren't required to use any particular programming language for this exercise, but Python is a good idea if you're up for it. We're a Python shop and you will be expected to learn the language if you don't already know it. Be sure to update this document with instructions on how to run your solution. Submit a pull request on GitHub when you're ready to have us take a look.
