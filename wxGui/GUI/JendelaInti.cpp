// -*- C++ -*-
//
// generated by wxGlade 9a4613e7dab8 on Thu Apr 20 07:45:05 2017 from "/home/richie/mygit/LearningPy/wxGui/GUI/JendelaInti.wxg"
//
// Example for compiling a single file project under Linux using g++:
//  g++ MyApp.cpp $(wx-config --libs) $(wx-config --cxxflags) -o MyApp
//
// Example for compiling a multi file project under Linux using g++:
//  g++ main.cpp $(wx-config --libs) $(wx-config --cxxflags) -o MyApp Dialog1.cpp Frame1.cpp
//

#include "JendelaInti.h"

// begin wxGlade: ::extracode
// end wxGlade



PanelJudul::PanelJudul(wxWindow* parent, wxWindowID id, const wxPoint& pos, const wxSize& size, long style):
    wxPanel(parent, id, pos, size, style)
{
    // begin wxGlade: PanelJudul::PanelJudul
    label_2 = new wxStaticText(this, wxID_ANY, _("APLIKASI PENJUALAN"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER);

    set_properties();
    do_layout();
    // end wxGlade
}


void PanelJudul::set_properties()
{
    // begin wxGlade: PanelJudul::set_properties
    // end wxGlade
}


void PanelJudul::do_layout()
{
    // begin wxGlade: PanelJudul::do_layout
    sizer_2 = new wxBoxSizer(wxVERTICAL);
    sizer_2->Add(label_2, 0, wxALIGN_CENTER|wxEXPAND, 0);
    SetSizer(sizer_2);
    sizer_2->Fit(this);
    // end wxGlade
}


JendelaInti::JendelaInti(wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style):
    wxFrame(parent, id, title, pos, size, wxDEFAULT_FRAME_STYLE)
{
    // begin wxGlade: JendelaInti::JendelaInti
    panel_2 = new wxPanel(this, wxID_ANY);
    notebook_2 = new wxNotebook(panel_2, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxNB_LEFT);
    Data_Barang_copy = new wxPanel(notebook_2, wxID_ANY);
    Penjualan_copy = new wxPanel(notebook_2, wxID_ANY);
    panel_12 = new wxPanel(Penjualan_copy, wxID_ANY);
    panel_11 = new wxPanel(Penjualan_copy, wxID_ANY);
    panel_9 = new wxPanel(Penjualan_copy, wxID_ANY);
    Menu_Utama_copy = new wxPanel(notebook_2, wxID_ANY);
    
    // Menu Bar
    Menu = new wxMenuBar();
    wxMenu* wxglade_tmp_menu;
    wxglade_tmp_menu = new wxMenu();
    wxMenuItem* wxglade_tmp_item;
    wxglade_tmp_item = wxglade_tmp_menu->Append(wxID_ANY, _("Keluar"), wxEmptyString);
    Bind(wxEVT_MENU, &JendelaInti::keluar, this, wxglade_tmp_item->GetId());
    Menu->Append(wxglade_tmp_menu, _("Berkas"));
    wxglade_tmp_menu = new wxMenu();
    wxglade_tmp_menu->Append(wxID_ANY, _("item"), wxEmptyString);
    Menu->Append(wxglade_tmp_menu, _("Pengaturan"));
    wxglade_tmp_menu = new wxMenu();
    wxglade_tmp_menu->Append(wxID_ANY, _("Laporan"), wxEmptyString);
    Menu->Append(wxglade_tmp_menu, _("Lihat"));
    wxglade_tmp_menu = new wxMenu();
    wxglade_tmp_item = wxglade_tmp_menu->Append(wxID_ANY, _("Bantuan"), wxEmptyString);
    Bind(wxEVT_MENU, &JendelaInti::bantuan, this, wxglade_tmp_item->GetId());
    Menu->Append(wxglade_tmp_menu, _("Informasi"));
    SetMenuBar(Menu);
    // Menu Bar end
    frame_statusbar = CreateStatusBar(1);
    frame_toolbar = new wxToolBar(this, -1, wxDefaultPosition, wxDefaultSize, wxTB_HORIZONTAL|wxTB_TEXT|wxTB_NOICONS);
    SetToolBar(frame_toolbar);
    frame_toolbar->AddTool(wxID_ANY, _("item"), wxNullBitmap, wxNullBitmap, wxITEM_NORMAL, wxEmptyString, wxEmptyString);
    frame_toolbar->AddTool(wxID_ANY, _("item"), wxNullBitmap, wxNullBitmap, wxITEM_NORMAL, wxEmptyString, wxEmptyString);
    frame_toolbar->AddTool(wxID_ANY, _("item"), wxNullBitmap, wxNullBitmap, wxITEM_NORMAL, wxEmptyString, wxEmptyString);
    frame_toolbar->AddTool(wxID_ANY, _("item"), wxNullBitmap, wxNullBitmap, wxITEM_NORMAL, wxEmptyString, wxEmptyString);
    frame_toolbar->AddTool(wxID_ANY, _("item"), wxNullBitmap, wxNullBitmap, wxITEM_NORMAL, wxEmptyString, wxEmptyString);
    frame_toolbar->Realize();
    panel_judul = new PanelJudul(this, wxID_ANY);
    bitmap_2 = new wxStaticBitmap(Menu_Utama_copy, wxID_ANY, wxBitmap(wxT("/home/richie/mygit/LearningPy/wxGui/GUI/images.png"), wxBITMAP_TYPE_ANY));
    panel_8 = new wxPanel(Penjualan_copy, wxID_ANY);
    panel_10 = new wxPanel(Penjualan_copy, wxID_ANY);
    text_ctrl_5 = new wxTextCtrl(panel_11, wxID_ANY, wxEmptyString);
    text_ctrl_6 = new wxTextCtrl(panel_11, wxID_ANY, _("1"), wxDefaultPosition, wxDefaultSize, wxTE_CENTRE);
    button_8 = new wxButton(panel_11, wxID_ADD, wxEmptyString);
    list_ctrl_2 = new wxListCtrl(Penjualan_copy, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxBORDER_DEFAULT|wxBORDER_SUNKEN|wxLC_REPORT|wxNO_FULL_REPAINT_ON_RESIZE);
    button_9 = new wxButton(Penjualan_copy, wxID_ANY, _("Cetak & Simpan"));
    button_2 = new wxButton(Penjualan_copy, wxID_ANY, _("Cetak Saja"));
    button_10 = new wxButton(Penjualan_copy, wxID_ANY, _("Hapus"));
    button_11 = new wxButton(Penjualan_copy, wxID_ANY, _("Lihat"));
    button_12 = new wxButton(Penjualan_copy, wxID_ANY, _("Pilihan Lainnya"), wxDefaultPosition, wxDefaultSize, wxBU_EXACTFIT);
    grid_2 = new wxGrid(Data_Barang_copy, wxID_ANY);
    Data_Pekerja_copy = new wxPanel(notebook_2, wxID_ANY);
    Pengaturan_copy = new wxPanel(notebook_2, wxID_ANY);

    set_properties();
    do_layout();
    // end wxGlade
}


void JendelaInti::set_properties()
{
    // begin wxGlade: JendelaInti::set_properties
    SetTitle(_("frame"));
    int frame_statusbar_widths[] = { -1 };
    frame_statusbar->SetStatusWidths(1, frame_statusbar_widths);

    // statusbar fields
    const wxString frame_statusbar_fields[] = {
        _("Status"),
    };
    for(int i = 0; i < frame_statusbar->GetFieldsCount(); ++i) {
        frame_statusbar->SetStatusText(frame_statusbar_fields[i], i);
    }
    panel_9->SetBackgroundColour(wxColour(255, 255, 0));
    text_ctrl_5->SetMinSize(wxSize(200, 34));
    button_9->SetMinSize(wxSize(150, 34));
    button_2->SetMinSize(wxSize(150, 34));
    button_10->SetMinSize(wxSize(150, 34));
    button_11->SetMinSize(wxSize(150, 34));
    button_12->SetMinSize(wxSize(150, 34));
    button_12->SetDefault();
    grid_2->CreateGrid(10, 5);
    grid_2->EnableEditing(false);
    grid_2->SetColLabelValue(0, _("KODE BARANG"));
    grid_2->SetColSize(0, 150);
    grid_2->SetColLabelValue(1, _("NAMA BARANG"));
    grid_2->SetColSize(1, 300);
    grid_2->SetColLabelValue(2, _("SATUAN"));
    grid_2->SetColSize(2, 75);
    grid_2->SetColLabelValue(3, _(" HARGA\n SATUAN"));
    grid_2->SetColSize(3, 100);
    grid_2->SetColLabelValue(4, _("KETERANGAN"));
    grid_2->SetColSize(4, 300);
    grid_2->SetFocus();
    Data_Barang_copy->SetBackgroundColour(wxColour(159, 159, 95));
    Data_Pekerja_copy->SetBackgroundColour(wxColour(159, 159, 95));
    Pengaturan_copy->SetBackgroundColour(wxColour(159, 159, 95));
    notebook_2->SetFont(wxFont(13, wxDEFAULT, wxNORMAL, wxNORMAL, 0, wxT("")));
    // end wxGlade
}


void JendelaInti::do_layout()
{
    // begin wxGlade: JendelaInti::do_layout
    sizer_3 = new wxBoxSizer(wxVERTICAL);
    wxBoxSizer* sizer_9 = new wxBoxSizer(wxVERTICAL);
    wxBoxSizer* sizer_15 = new wxBoxSizer(wxVERTICAL);
    wxBoxSizer* sizer_11 = new wxBoxSizer(wxVERTICAL);
    wxBoxSizer* sizer_14 = new wxBoxSizer(wxHORIZONTAL);
    wxGridSizer* grid_sizer_6 = new wxGridSizer(5, 1, 0, 0);
    wxBoxSizer* sizer_12 = new wxBoxSizer(wxVERTICAL);
    wxGridSizer* grid_sizer_5 = new wxGridSizer(3, 3, 0, 0);
    wxFlexGridSizer* grid_sizer_4 = new wxFlexGridSizer(1, 7, 0, 0);
    wxBoxSizer* sizer_13 = new wxBoxSizer(wxVERTICAL);
    wxBoxSizer* sizer_10 = new wxBoxSizer(wxVERTICAL);
    sizer_3->Add(panel_judul, 1, wxEXPAND, 0);
    sizer_10->Add(bitmap_2, 2, wxEXPAND, 0);
    Menu_Utama_copy->SetSizer(sizer_10);
    sizer_12->Add(panel_8, 0, 0, 0);
    wxStaticText* label_7 = new wxStaticText(panel_9, wxID_ANY, _("0"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER|wxALIGN_RIGHT);
    label_7->SetFont(wxFont(50, wxDEFAULT, wxNORMAL, wxNORMAL, 0, wxT("")));
    sizer_13->Add(label_7, 1, wxALIGN_RIGHT, 0);
    panel_9->SetSizer(sizer_13);
    sizer_12->Add(panel_9, 0, wxEXPAND, 0);
    sizer_12->Add(panel_10, 0, 0, 0);
    wxStaticText* label_8 = new wxStaticText(panel_11, wxID_ANY, _("Kode Barang"));
    grid_sizer_4->Add(label_8, 0, wxALIGN_CENTER|wxLEFT, 8);
    grid_sizer_4->Add(text_ctrl_5, 0, wxLEFT|wxRIGHT, 8);
    wxStaticText* label_9 = new wxStaticText(panel_11, wxID_ANY, _("Jumlah"));
    grid_sizer_4->Add(label_9, 0, wxALIGN_CENTER, 0);
    grid_sizer_4->Add(text_ctrl_6, 0, wxALIGN_CENTER|wxLEFT|wxRIGHT, 8);
    grid_sizer_4->Add(button_8, 0, wxRIGHT, 8);
    panel_11->SetSizer(grid_sizer_4);
    sizer_12->Add(panel_11, 0, wxEXPAND, 0);
    grid_sizer_5->Add(0, 0, 0, 0, 0);
    grid_sizer_5->Add(0, 0, 0, 0, 0);
    grid_sizer_5->Add(0, 0, 0, 0, 0);
    grid_sizer_5->Add(0, 0, 0, 0, 0);
    grid_sizer_5->Add(0, 0, 0, 0, 0);
    grid_sizer_5->Add(0, 0, 0, 0, 0);
    grid_sizer_5->Add(0, 0, 0, 0, 0);
    grid_sizer_5->Add(0, 0, 0, 0, 0);
    grid_sizer_5->Add(0, 0, 0, 0, 0);
    panel_12->SetSizer(grid_sizer_5);
    sizer_12->Add(panel_12, 0, wxEXPAND, 0);
    sizer_11->Add(sizer_12, 1, wxEXPAND, 0);
    sizer_14->Add(list_ctrl_2, 5, wxEXPAND, 0);
    grid_sizer_6->Add(button_9, 0, 0, 0);
    grid_sizer_6->Add(button_2, 0, 0, 0);
    grid_sizer_6->Add(button_10, 0, 0, 0);
    grid_sizer_6->Add(button_11, 0, 0, 0);
    grid_sizer_6->Add(button_12, 0, 0, 0);
    sizer_14->Add(grid_sizer_6, 1, wxLEFT|wxRIGHT, 10);
    sizer_11->Add(sizer_14, 5, wxEXPAND, 0);
    Penjualan_copy->SetSizer(sizer_11);
    sizer_15->Add(0, 0, 0, 0, 0);
    sizer_15->Add(grid_2, 3, wxEXPAND, 0);
    Data_Barang_copy->SetSizer(sizer_15);
    notebook_2->AddPage(Menu_Utama_copy, _("Menu Utama"));
    notebook_2->AddPage(Penjualan_copy, _("Penjualan"));
    notebook_2->AddPage(Data_Barang_copy, _("Data Barang"));
    notebook_2->AddPage(Data_Pekerja_copy, _("Data Pekerja"));
    notebook_2->AddPage(Pengaturan_copy, _("Pengaturan"));
    sizer_9->Add(notebook_2, 5, wxALIGN_CENTER|wxEXPAND, 0);
    panel_2->SetSizer(sizer_9);
    sizer_3->Add(panel_2, 1, wxEXPAND, 0);
    SetSizer(sizer_3);
    sizer_3->Fit(this);
    sizer_3->SetSizeHints(this);
    Layout();
    Centre();
    // end wxGlade
}


BEGIN_EVENT_TABLE(JendelaInti, wxFrame)
    // begin wxGlade: JendelaInti::event_table
    EVT_BUTTON(wxID_ANY, JendelaInti::Input)
    EVT_BUTTON(wxID_ANY, JendelaInti::pilihan_lainnya)
    // end wxGlade
END_EVENT_TABLE();


void JendelaInti::keluar(wxCommandEvent &event)
{
    event.Skip();
    // notify the user that he hasn't implemented the event handler yet
    wxLogDebug(wxT("Event handler (JendelaInti::keluar) not implemented yet"));
}

void JendelaInti::bantuan(wxCommandEvent &event)
{
    event.Skip();
    // notify the user that he hasn't implemented the event handler yet
    wxLogDebug(wxT("Event handler (JendelaInti::bantuan) not implemented yet"));
}

void JendelaInti::Input(wxCommandEvent &event)
{
    event.Skip();
    // notify the user that he hasn't implemented the event handler yet
    wxLogDebug(wxT("Event handler (JendelaInti::Input) not implemented yet"));
}

void JendelaInti::pilihan_lainnya(wxCommandEvent &event)
{
    event.Skip();
    // notify the user that he hasn't implemented the event handler yet
    wxLogDebug(wxT("Event handler (JendelaInti::pilihan_lainnya) not implemented yet"));
}


// wxGlade: add JendelaInti event handlers


class MyApp: public wxApp {
public:
    bool OnInit();
protected:
    wxLocale m_locale;  // locale we'll be using
};

IMPLEMENT_APP(MyApp)

bool MyApp::OnInit()
{
    m_locale.Init();
#ifdef APP_LOCALE_DIR
    m_locale.AddCatalogLookupPathPrefix(wxT(APP_LOCALE_DIR));
#endif
    m_locale.AddCatalog(wxT(APP_CATALOG));

    wxInitAllImageHandlers();
    JendelaInti* JendelaInti = new JendelaInti(NULL, wxID_ANY, wxEmptyString);
    SetTopWindow(JendelaInti);
    JendelaInti->Show();
    return true;
}