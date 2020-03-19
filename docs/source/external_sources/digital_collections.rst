===================
Digital Collections
===================

Metadata Mapping
================

This metadata mapping maps Islandora MODS to Primo VE DublinCore Expanded based on the
`Mapping to the Display, Facets, and Search Sections in the Primo VE Record <https://knowledge.exlibrisgroup.com/Primo/Product_Documentation/020Primo_VE/050Other_Configuration/Mapping_to_the_Display%2C_Facets%2C_and_Search_Sections_in_the_Primo_VE_Record#Dublin_Core_2>`_
and the `Configuring Import Profiles for Primo VE <https://knowledge.exlibrisgroup.com/Primo/Product_Documentation/020Primo_VE/045Loading_Records_from_External_Sources_into_Primo_VE/Configuring_Import_Profiles_for_Primo_VE>`_ documentation.

| ﻿MODS                                                                                                    | Primo VE Expanded DublinCore | Display Field                   | Facets Field           | Search Field           | Notes                                                                                                                                                                                                                                                                                                                                                          |
|---------------------------------------------------------------------------------------------------------|------------------------------|---------------------------------|------------------------|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| mods:titleInfo/mods:title OR mods:titleInfo[@supplied="yes"]/title                                      | dc:title                     | Title                           |                        | Title                  |                                                                                                                                                                                                                                                                                                                                                                |
| mods:identifier                                                                                         | dc:identifier                |                                 |                        | General                |                                                                                                                                                                                                                                                                                                                                                                |
| mods:abstract                                                                                           | dcterms:abstract             | Description                     | Description            | Description            |                                                                                                                                                                                                                                                                                                                                                                |
| mods:tableOfContents                                                                                    | dcterms.tableOfContents      |                                 |                        | Table of Contents      |                                                                                                                                                                                                                                                                                                                                                                |
| mods:originInfo/mods:dateIssued AND mods:originInfo/mods:dateCreated AND mods:originInfo/mods:dateOther | dcterms:date                 | Creation Date                   | Creation Date          | Creation Date          |                                                                                                                                                                                                                                                                                                                                                                |
| mods:name/mods:namePart                                                                                 | dc:creator                   | Creator                         | Creator & Contributors | Creator & Contributors | Creator roles include: Creator, Author, Photographer, Illustrator, Composer, Performer, Lyricist, Artist, Lithographer, Cartographer, Engraver, Designer, Architect, Interviewee                                                                                                                                                                               |
| mods:name/mods:namePart                                                                                 | dc:contributor               | Contributor                     | Creator & Contributors | Creator & Contributors | Contributor roles include: Editor, Copyright holder, Contributor, Production company, Stage director, Musical director, Arranger, Issuing body, Attributed name, Standards body, Other, Donor, Client, Contractor, Former owner, Originator, Owner, Printer, Publisher, Compiler, Honoree, Printer of plates, Distributor, Correspondent, Interviewer, Witness |
| mods:originInfo/mods:publisher                                                                          | dcterms:publisher            | Publisher                       |                        | General                |                                                                                                                                                                                                                                                                                                                                                                |
| mods:physicalDescription/mods:form                                                                      | dcterms:extent               | Physical Description and Format |                        | Format                 |                                                                                                                                                                                                                                                                                                                                                                |
| mods:subject/mods:topic                                                                                 | dc:subject                   | Subjects                        | Topic                  | Subjects               |                                                                                                                                                                                                                                                                                                                                                                |
| mods:subject/mods:geographic and mods:subject/mods:temporal                                             | dcterms:coverage             |                                 |                        | General                |                                                                                                                                                                                                                                                                                                                                                                |
| mods:language/mods:languageTerm                                                                         | dcterms:language             | Language                        | Language               | Language               |                                                                                                                                                                                                                                                                                                                                                                |
| mods:accessCondition                                                                                    | dcterms:accessRights         | Rights                          |                        |                        |                                                                                                                                                                                                                                                                                                                                                                |
| mods:typeOfResource[@collection="yes"]                                                                  | discovery:resourceType       |                                 |                        |                        |                                                                                                                                                                                                                                                                                                                                                                |
| mods:typeOfResource[not(@collection="yes")]                                                             | discovery:resourceType       |                                 |                        |                        |                                                                                                                                                                                                                                                                                                                                                                |

Discovery Import Profile
========================

Normalization Rules
===================

.. code-block:: xml
    :name: Sample XML Record
    :caption: Sample XML Record

    <?xml version="1.0" encoding="UTF-8"?>
    <record>
        <header>
            <identifier>vanvactor_6981</identifier>
            <datestamp>2020-03-03T04:01:39Z</datestamp>
            <setSpec>vanvactor</setSpec>
        </header>
        <metadata>
            <mods xmlns="http://www.loc.gov/mods/v3" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.loc.gov/mods/v3 http://www.loc.gov/standards/mods/v3/mods-3-5.xsd">
                <identifier type="local">0012_003979_000345</identifier>
                <identifier type="pid">vanvactor:6981</identifier>
                <titleInfo>
                    <title>Quartet no. 2</title>
                </titleInfo>
                <abstract>Pencil score and sketches with pen markings.</abstract>
                <tableOfContents>Allegro alla marcia - Lento - Allegro moderato</tableOfContents>
                <note type="instrumentation">For 2 violins, viola, and cello.</note>
                <genre authority="lcmpt" valueURI="http://id.loc.gov/authorities/performanceMediums/mp2013015782">violin</genre>
                <genre authority="lcmpt" valueURI="http://id.loc.gov/authorities/performanceMediums/mp2013015772">viola</genre>
                <genre authority="lcmpt" valueURI="http://id.loc.gov/authorities/performanceMediums/mp2013015120">cello</genre>
                <originInfo>
                    <dateCreated>1950</dateCreated>
                    <dateCreated encoding="edtf" keyDate="yes">1950</dateCreated>
                </originInfo>
                <physicalDescription>
                    <form authority="aat" valueURI="http://vocab.getty.edu/aat/300026427">scores (documents for music)</form>
                    <extent>15 pages</extent>
                    <internetMediaType>pdf</internetMediaType>
                </physicalDescription>
                <name valueURI="http://id.loc.gov/authorities/names/n82001311">
                    <namePart>Van Vactor, David, 1906-1994</namePart>
                    <role>
                        <roleTerm authority="marcrelator" valueURI="http://id.loc.gov/vocabulary/relators/cmp">Composer</roleTerm>
                    </role>
                </name>
                <subject authority="lcsh" valueURI="http://id.loc.gov/authorities/subjects/sh85129035">
                    <topic>String quartets</topic>
                </subject>
                <subject authority="lcsh" valueURI="http://id.loc.gov/authorities/subjects/sh85088803">
                    <topic>Music--Manuscripts</topic>
                </subject>
                <genre authority="lcgft" valueURI="http://id.loc.gov/authorities/genreForms/gf2014026704">Chamber music</genre>
                <genre authority="lcgft" valueURI="http://id.loc.gov/authorities/subjects/sh99001779">Scores</genre>
                <relatedItem type="otherVersion">
                    <titleInfo>
                        <title>String quartet no. 2</title>
                    </titleInfo>
                    <identifier type="catalog">M101</identifier>
                </relatedItem>
                <typeOfResource>notated music</typeOfResource>
                <relatedItem displayLabel="Project" type="host">
                    <titleInfo>
                        <title>David Van Vactor Music Collection</title>
                    </titleInfo>
                </relatedItem>
                <relatedItem displayLabel="Collection" type="host">
                    <titleInfo>
                        <title>David Van Vactor Papers</title>
                    </titleInfo>
                    <identifier>MS.1942</identifier>
                    <location>
                        <url>https://n2t.net/ark:/87290/v8pz5703</url>
                    </location>
                </relatedItem>
                <location>
                    <physicalLocation valueURI="http://id.loc.gov/authorities/names/no2014027633">
                        University of Tennessee, Knoxville. Special Collections
                    </physicalLocation>
                    <url access="object in context" usage="primary display">
                        https://digital.lib.utk.edu/collections/islandora/object/vanvactor%3A6981
                    </url>
                    <url access="preview">
                        https://digital.lib.utk.edu/collections/islandora/object/vanvactor%3A6981/datastream/TN/view
                    </url>
                </location>
                <recordInfo>
                    <recordContentSource valueURI="http://id.loc.gov/authorities/names/n87808088">University of Tennessee, Knoxville. Libraries</recordContentSource>
                </recordInfo>
                <accessCondition type="use and reproduction" xlink:href="http://rightsstatements.org/vocab/InC/1.0/">In Copyright</accessCondition>
            </mods>
        </metadata>
    </record>
    

.. code-block:: rst
    :name: Display identifier
    :caption: Display identifier

    rule "Display identifier"
		when
			exist "//metadata//*[local-name()='identifier'][@type='local']"
		then
			copy "//metadata//*[local-name()='identifier'][@type='local']" to "dc"."identifier"
	end


.. code-block:: rst
    :name: Copy one supplied title if available
    :caption: Copy one supplied title if available

	rule "Copy one supplied title if available"
		when 
			exist "/*[local-name()='record']/*[local-name()='metadata']/*[local-name()='mods']/*[local-name()='titleInfo'][@supplied]/*[local-name()='title']"
		then
			copy "(/*[local-name()='record']/*[local-name()='metadata']/*[local-name()='mods']/*[local-name()='titleInfo'][@supplied]/*[local-name()='title'])[1]" to "dc"."title"
		end

.. code-block:: rst
    :name: Copy one transcribed title if no supplied title
    :caption: Copy one transcribed title if no supplied title

	rule "Copy one transcribed title if no supplied title"
		when
			not exist "/*[local-name()='record']/*[local-name()='metadata']/*[local-name()='mods']/*[local-name()='titleInfo'][@supplied]/*[local-name()='title']"
		then
			copy "(/*[local-name()='record']/*[local-name()='metadata']/*[local-name()='mods']/*[local-name()='titleInfo'][not(@supplied)]/*[local-name()='title'])[1]" to "dc"."title"
	end

.. code-block:: rst
    :name: Copy description
    :caption: Copy description

	rule "Copy description"
		when
			exist "/*[local-name()='record']/*[local-name()='metadata']/*[local-name()='mods']/*[local-name()='abstract']"
		then
			copy "/*[local-name()='record']/*[local-name()='metadata']/*[local-name()='mods']/*[local-name()='abstract']" to "dcterms." "abstract"
	end

.. code-block:: rst
    :name: Copy note if not DPN
    :caption: Copy note if not DPN

	rule "Copy note if not DPN"
		when
			exist "/*[local-name()='record']/*[local-name()='metadata']/*[local-name()='mods']/*[local-name()='note'][not(@displayLabel='dpn')]"
		then
			copy "/*[local-name()='record']/*[local-name()='metadata']/*[local-name()='mods']/*[local-name()='note'][not(@displayLabel='dpn')]" to "dc." "description"
	end

.. code-block::
    :name: Copy table of contents
    :caption: Copy table of contents

	rule "Copy table of contents"
		when
			exist "/*[local-name()='record']/*[local-name()='metadata']/*[local-name()='mods']/*[local-name()='tableOfContents']"
		then
			copy "/*[local-name()='record']/*[local-name()='metadata']/*[local-name()='mods']/*[local-name()='tableOfContents']" to "dcterms." "tableOfContents"
	end


.. code-block::
    :name: Copy creation date
    :caption: Copy creation date

	rule "Copy creation date"
		when
			exist "/*[local-name()='record']/*[local-name()='metadata']/*[local-name()='mods']/*[local-name()='originInfo']/*[local-name()='dateCreated'][not(@encoding)]"
		then
			copy "/*[local-name()='record']/*[local-name()='metadata']/*[local-name()='mods']/*[local-name()='originInfo']/*[local-name()='dateCreated'][not(@encoding)]" to "dc"."date"
	end

.. code-block::
    :name: Copy publication date
    :caption: Copy publication date

	rule "Copy publication date"
		when
			exist "/*[local-name()='record']/*[local-name()='metadata']/*[local-name()='mods']/*[local-name()='originInfo']/*[local-name()='dateIssued'][not(@encoding)]"
		then
			copy "/*[local-name()='record']/*[local-name()='metadata']/*[local-name()='mods']/*[local-name()='originInfo']/*[local-name()='dateIssued'][not(@encoding)]" to "dc"."date"
	end

.. code-block::
    :name: Copy miscellaneous date
    :caption: Copy miscellaneous date

	rule "Copy miscellaneous date"
		when
			exist "/*[local-name()='record']/*[local-name()='metadata']/*[local-name()='mods']/*[local-name()='originInfo']/*[local-name()='dateOther'][not(@encoding)]"
		then
			copy "/*[local-name()='record']/*[local-name()='metadata']/*[local-name()='mods']/*[local-name()='originInfo']/*[local-name()='dateOther'][not(@encoding)]" to "dc"."date"
	end

.. code-block::
    :name: Copy publisher
    :caption: Copy publisher

	rule "Copy publisher"
		when
			exist "/*[local-name()='record']/*[local-name()='metadata']/*[local-name()='mods']/*[local-name()='originInfo']/*[local-name()='publisher']"
		then
			copy "/*[local-name()='record']/*[local-name()='metadata']/*[local-name()='mods']/*[local-name()='originInfo']/*[local-name()='publisher']" to "dcterms"."publisher"
	end

.. code-block::
    :name: Copy format
    :caption: Copy format

	rule "Copy format"
		when
			exist "/*[local-name()='record']/*[local-name()='metadata']/*[local-name()='mods']/*[local-name()='physicalDescription']/*[local-name()='form']"
		then
			copy "/*[local-name()='record']/*[local-name()='metadata']/*[local-name()='mods']/*[local-name()='physicalDescription']/*[local-name()='form']" to "dcterms"."extent"
	end

.. code-block::
    :name: Copy all topical subjects
    :caption: Copy all topical subjects

	rule "Copy all topical subjects"
		when
			exist "/*[local-name()='record']/*[local-name()='metadata']/*[local-name()='mods']/*[local-name()='subject']/*[local-name()='topic']"
		then
			copy "/*[local-name()='record']/*[local-name()='metadata']/*[local-name()='mods']/*[local-name()='subject']/*[local-name()='topic']" to "dc"."subject"
	end

.. code-block::
    :name: Copy all geographic subjects
    :caption: Copy all geographic subjects

	rule "Copy all geographic subjects"
		when
			exist "/*[local-name()='record']/*[local-name()='metadata']/*[local-name()='mods']/*[local-name()='subject']/*[local-name()='geographic']"
		then
			copy "/*[local-name()='record']/*[local-name()='metadata']/*[local-name()='mods']/*[local-name()='subject']/*[local-name()='geographic']" to "dcterms"."coverage"
	end

.. code-block::
    :name: Copy rights values
    :caption: Copy rights values

	rule "Copy rights values"
		when
			exist "/*[local-name()='record']/*[local-name()='metadata']/*[local-name()='mods']/*[local-name()='accessCondition']"
		then 
			copy "/*[local-name()='record']/*[local-name()='metadata']/*[local-name()='mods']/*[local-name()='accessCondition']" to "dcterms"."accessRights"
	end

.. code-block::
    :name: Set discovery resource type of Digital Collections Item
    :caption: Set discovery resource type of Digital Collections Item

	rule "Set discovery resource type of Digital Collections Item"
    	when
        	exist "/*[local-name()='record']/*[local-name()='metadata']/*[local-name()='mods']/*[local-name()='typeOfResource'][not(@collection='yes')]"
    	then
        	set "digital_items" in "discovery"."resourceType"
	end

.. code-block::
    :name: Set discovery resource type of Digital Collection
    :caption: Set discovery resource type of Digital Collection

	rule "Set discovery resource type of Digital Collection"
    	when
         	exist "/*[local-name()='record']/*[local-name()='metadata']/*[local-name()='mods']/*[local-name()='typeOfResource'][@collection='yes']"   
    	then
        	set "digital_collection" in "discovery"."resourceType"
	end